#!/usr/bin/env python3
import json
import time

def search_law(query, limit=5):
    """
    Mock function to search for laws and regulations.
    """
    print(f"[API] Searching Laws for: '{query}'...")
    time.sleep(0.5) # Simulate network latency
    
    # Mock Response
    results = [
        {
            "title": "中华人民共和国民法典",
            "effective_date": "2021-01-01",
            "status": "Effective",
            "snippet": "...本法是为了保护民事主体的合法权益..."
        },
        {
            "title": "最高人民法院关于适用《中华人民共和国民法典》合同编通则若干问题的解释",
            "effective_date": "2023-12-05",
            "status": "Effective",
            "snippet": "...为正确审理合同纠纷案件..."
        }
    ]
    return results[:limit]

def search_case(query, limit=3):
    """
    Mock function to search for judicial cases.
    """
    print(f"[API] Searching Cases for: '{query}'...")
    time.sleep(0.8)
    
    # Mock Response
    results = [
        {
            "case_name": "XX公司与XX员工劳动争议案",
            "case_no": "(2023)京01民终1234号",
            "court": "北京市第一中级人民法院",
            "summary": "法院认为，劳动者违反竞业限制协议，应当支付违约金..."
        },
        {
            "case_name": "指导案例XXX号：XX诉XX公司股权转让纠纷案",
            "case_no": "(2020)最高法民终888号",
            "court": "最高人民法院",
            "summary": "裁判要旨：对赌协议中关于股权回购的约定，不因未履行减资程序而归于无效..."
        }
    ]
    return results[:limit]

if __name__ == "__main__":
    print("--- Simulating PKULaw API Search ---")
    q = "竞业限制 AND 违约金"
    
    laws = search_law(q)
    print(f"\nFound {len(laws)} Laws:")
    print(json.dumps(laws, indent=2, ensure_ascii=False))
    
    cases = search_case(q)
    print(f"\nFound {len(cases)} Cases:")
    print(json.dumps(cases, indent=2, ensure_ascii=False))
