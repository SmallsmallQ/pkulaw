import sys
import argparse
import time
import random
from docx import Document
from docx.oxml.shared import OxmlElement
from docx.oxml import parse_xml # Added import
from docx.oxml.ns import qn
from docx.opc.constants import CONTENT_TYPE as CT
from docx.opc.part import Part
from docx.opc.packuri import PackURI

# Microsoft Word Namespaces
NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_COMMENTS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"

def get_or_create_comments_part(doc):
    """
    Retrieves the comments part of the document. If it doesn't exist, creates it.
    """
    part = doc.part
    # Check if comments part exists
    try:
        comments_part = part.part_related_by(CT.WML_COMMENTS)
    except KeyError:
        comments_part = None

    if comments_part is None:
        # Create a new comments part
        target_uri = PackURI("/word/comments.xml")
        comments_part = Part(
            partname=target_uri,
            content_type=CT.WML_COMMENTS,
            blob=b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"></w:comments>',
            package=doc.part.package
        )
        part.relate_to(comments_part, NS_COMMENTS_REL)
    
    return comments_part

def add_comment_xml(comments_part, author, initials, comment_text):
    """
    Adds a comment to the comments.xml part and returns its ID.
    """
    # Parse the comments XML from the part's blob
    comments_element = parse_xml(comments_part.blob)
    
    # Generate a new ID (find max ID and increment)
    existing_ids = [int(c.get(qn('w:id'))) for c in comments_element.findall(qn('w:comment'))]
    new_id = max(existing_ids) + 1 if existing_ids else 1
    new_id_str = str(new_id)

    # Create the <w:comment> element
    comment = OxmlElement('w:comment')
    comment.set(qn('w:id'), new_id_str)
    comment.set(qn('w:author'), author)
    comment.set(qn('w:initials'), initials)
    # Using current time for date, format: 2023-10-27T10:00:00Z
    # For simplicity in this script, we can omit date or use a fixed format if needed
    # comment.set(qn('w:date'), ...) 

    # Create paragraph for comment text
    p = OxmlElement('w:p')
    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.text = comment_text
    
    r.append(t)
    p.append(r)
    comment.append(p)
    
    comments_element.append(comment)
    
    # Update the part's blob with the modified XML
    comments_part._blob = comments_element.xml
    
    
    return new_id_str

def insert_comment_reference(paragraph, run, comment_id):
    """
    Wraps the 'run' in a comment range and adds a comment reference.
    """
    # Create start tag
    start = OxmlElement('w:commentRangeStart')
    start.set(qn('w:id'), comment_id)
    
    # Create end tag
    end = OxmlElement('w:commentRangeEnd')
    end.set(qn('w:id'), comment_id)
    
    # Create reference tag
    reference = OxmlElement('w:commentReference')
    reference.set(qn('w:id'), comment_id)
    
    # Insert start before the run
    # We need to find the parent of the run (which is the paragraph element)
    # and insert 'start' before 'run', and 'end' after 'run', then 'reference'.
    
    # CAUTION: 'run' is a wrapper, we need the underlying xml element
    r_element = run._r
    p_element = paragraph._p
    
    # Find index of run element in paragraph
    try:
        index = list(p_element).index(r_element)
    except ValueError:
        print("Error: Run not found in paragraph elements.")
        return

    # Insert commentRangeStart before the run
    p_element.insert(index, start)
    
    # Insert commentRangeEnd after the run (now index + 2 because we added start)
    # But simpler: insert after the run
    p_element.insert(index + 2, end)
    
    # Insert commentReference after the end
    # We create a new run for the reference to make it cleaner visually usually, 
    # or just insert the reference node. Word expects reference inside a run usually for valid XML?
    # Actually w:commentReference is a run-level element usually placed inside a w:r/w:commentReference or standalone?
    # Spec says w:commentReference is a child of w:r usually? No, it's child of p.
    # Wait, check spec: w:commentReference is a child of w:p. Correct.
    
    # However, to be safe, sometimes it's wrapped in a run with formatting 
    # style 'CommentReference'. But bare element works too.
    
    # Let's wrap it in a run to be safe and standard
    ref_run = OxmlElement('w:r')
    ref_run.append(reference)
    p_element.insert(index + 3, ref_run)


def add_comment_to_run_containing_text(doc, target_text, comment_text, author, initials):
    """
    Finds the first run containing the target_text and adds a comment to it.
    Current limitation: Assumes target_text is within a single run.
    """
    comments_part = get_or_create_comments_part(doc)
    
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if target_text in run.text:
                # Found it
                comment_id = add_comment_xml(comments_part, author, initials, comment_text)
                insert_comment_reference(paragraph, run, comment_id)
                return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Add native Word comments to a docx file.")
    parser.add_argument("file_path", help="Path to the input .docx file")
    parser.add_argument("target_text", help="Text to highlight and comment on")
    parser.add_argument("comment_text", help="Electronic comment text")
    parser.add_argument("--author", default="AI Reviewer", help="Author name for the comment")
    
    args = parser.parse_args()
    
    try:
        doc = Document(args.file_path)
        
        success = add_comment_to_run_containing_text(
            doc, 
            args.target_text, 
            args.comment_text, 
            args.author, 
            "AI"
        )
        
        if success:
            output_path = args.file_path.replace(".docx", "_reviewed.docx")
            if output_path == args.file_path: output_path = args.file_path + "_reviewed.docx"
            doc.save(output_path)
            print(f"Success: Comment added. Saved to {output_path}")
        else:
            print(f"Failure: Target text '{args.target_text}' not found in any single run.")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
