#!/usr/bin/env python3
import os
import httpx
import json

# API Configuration
LAW_SEARCH_URL = "https://apim-gateway.pkulaw.com/mcp-law"
CASE_SEARCH_URL = "https://apim-gateway.pkulaw.com/mcp-case"
CITATION_VALIDATOR_URL = "https://apim-gateway.pkulaw.com/pku_citation_validator"

def get_token():
    token = os.environ.get("PKULAW_API_TOKEN")
    if not token:
        raise ValueError("Missing PKULaw API Token. Please set PKULAW_API_TOKEN environment variable.")
    return token

def search_law(query, limit=5):
    """
    Search for laws and regulations using PKULaw API (Keyword Search).
    """
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    # Adjust payload based on actual API requirement. 
    # Assuming standard JSON payload: {"query": "...", "limit": ...} based on user description "Keyword"
    # Actually user didn't specify payload format, just URL. 
    # Standard MCP patterns usually POST {"query": ...}. 
    # Let's try to infer or use a generic query param if GET, or JSON if POST.
    # Given "streamablehttp", likely POST. Let's assume standard MCP-like payload or simple JSON.
    
    payload = {
        "query": query,
        "limit": limit
    }
    
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(LAW_SEARCH_URL, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return {"error": f"API Request Failed: {str(e)}", "details": str(e)}

def search_case(query, limit=5):
    """
    Search for cases using PKULaw API (Keyword Search).
    """
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": query,
        "limit": limit
    }
    
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(CASE_SEARCH_URL, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        return {"error": f"API Request Failed: {str(e)}", "details": str(e)}

if __name__ == "__main__":
    # Simple test if run directly
    try:
        print(search_law("民法典", 1))
    except ValueError as e:
        print(e)
