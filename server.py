from fastmcp import FastMCP
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure scripts directory is in python path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

try:
    # TRY to import real API first
    try:
        from scripts.pkulaw_api import search_law, search_case
    except ImportError:
        # Fallback to mock if file missing (shouldn't happen in prod)
        from scripts.mock_pkulaw_api import search_law, search_case
        
    from scripts.docx_annotator import add_comment_to_run_containing_text
    from docx import Document
except ImportError as e:
    print(f"Error importing scripts: {e}")
    sys.exit(1)

# Initialize FastMCP server
mcp = FastMCP("pkulaw")

@mcp.tool()
def search_laws(query: str, limit: int = 5) -> str:
    """
    Search for laws and regulations in the PKULaw database.
    Requires PKULaw API Token configured specific via env var PKULAW_API_TOKEN.
    
    Args:
        query: The search keywords.
        limit: Maximum number of results to return (default 5).
    """
    if not os.environ.get("PKULAW_API_TOKEN"):
        return "Error: Missing API Token. Please set 'PKULAW_API_TOKEN' environment variable or in .env file."

    try:
        results = search_law(query, limit)
        return str(results)
    except Exception as e:
        return f"Error searching laws: {str(e)}"

@mcp.tool()
def search_cases(query: str, limit: int = 5) -> str:
    """
    Search for judicial cases in the PKULaw database.
    Requires PKULaw API Token configured specific via env var PKULAW_API_TOKEN.
    
    Args:
        query: The search keywords.
        limit: Maximum number of results to return (default 5).
    """
    if not os.environ.get("PKULAW_API_TOKEN"):
        return "Error: Missing API Token. Please set 'PKULAW_API_TOKEN' environment variable or in .env file."

    try:
        results = search_case(query, limit)
        return str(results)
    except Exception as e:
        return f"Error searching cases: {str(e)}"

@mcp.tool()
def annotate_document(file_path: str, target_text: str, comment: str, author: str = "AI") -> str:
    """
    Add a comment to a Word document (.docx) on a specific text snippet.
    
    Args:
        file_path: Absolute path to the .docx file.
        target_text: The text to highlight and comment on.
        comment: The content of the comment.
        author: The author name to display (default "AI").
    """
    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path}"
    
    try:
        doc = Document(file_path)
        success = add_comment_to_run_containing_text(doc, target_text, comment, author, "AI")
        
        if success:
            output_path = file_path.replace(".docx", "_reviewed.docx")
            if output_path == file_path: output_path = output_path + "_reviewed.docx"
            
            doc.save(output_path)
            return f"Success: Comment added. Saved to {output_path}"
        else:
            return f"Failure: Target text '{target_text}' not found in the document."
    except Exception as e:
        return f"Error processing document: {str(e)}"

if __name__ == "__main__":
    mcp.run()
