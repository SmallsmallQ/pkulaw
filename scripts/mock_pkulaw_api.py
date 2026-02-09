#!/usr/bin/env python3
import json
import time
import argparse

def search_law(query, limit=5):
    """
    Mock function to search for laws and regulations.
    """
    # print(f"[API] Searching Laws for: '{query}'...")
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
        },
        {
            "title": "中华人民共和国刑法",
            "effective_date": "1979-07-01",
            "status": "Effective",
            "snippet": "...为了惩罚犯罪，保护人民..."
        },
        {
            "title": "中华人民共和国著作权法",
            "effective_date": "1991-06-01",
            "status": "Effective",
            "snippet": "...为保护文学、艺术和科学作品作者的著作权..."
        },
        {
            "title": "中华人民共和国专利法",
            "effective_date": "1985-04-01",
            "status": "Effective",
            "snippet": "...为了保护发明创造专利权..."
        }
    ]
    return results[:limit]

def search_case(query, limit=3):
    """
    Mock function to search for judicial cases.
    """
    # print(f"[API] Searching Cases for: '{query}'...")
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
        },
        {
            "case_name": "张三诉李四房屋买卖合同纠纷案",
            "case_no": "(2022)沪01民初5678号",
            "court": "上海市浦东新区人民法院",
            "summary": "法院认定，双方签订的房屋买卖合同合法有效，判决李四继续履行合同..."
        }
    ]
    return results[:limit]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mock PKULaw API for legal research.")
    parser.add_argument("action", choices=["search_law", "search_case"], help="Action to perform: search_law or search_case")
    parser.add_argument("--query", required=True, help="Search query string.")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of results to return.")

    args = parser.parse_args()

    if args.action == "search_law":
        results = search_law(args.query, args.limit)
    elif args.action == "search_case":
        results = search_case(args.query, args.limit)
    else:
        results = {"error": "Invalid action specified."}

    print(json.dumps(results, indent=2, ensure_ascii=False))
