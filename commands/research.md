# 法律检索与研究 (Research)

该指令用于辅助进行深度法律问题研究。不同于简单的关键词搜索，本指令包含一个**交互式需求澄清**阶段，确保在开始检索前准确理解研究目标、法律管辖和产出要求。

## 核心工作流 (Core Workflow)

1.  **需求澄清 (Requirement Elicitation)**：系统主动提出关键问题，锁定研究方向。
2.  **策略制定 (Strategy Formulation)**：根据需求构建检索关键词和逻辑路径。
3.  **信息检索 (Information Retrieval)**：执行多源法律检索（法规、案例、期刊）。
4.  **整合分析 (Synthesis & Analysis)**：对检索结果进行筛选、提炼和逻辑整合。

## 使用方法 (Usage)

```bash
/research [Topic/Query]
```

### 交互式问卷 (Pre-research Questionnaire)

当用户输入模糊或宽泛的研究请求时，系统将**优先**提出以下问题供用户选择或补充，以确定研究画像：

> **请回答以下问题以启动研究：**
>
> 1.  **司法管辖区 (Jurisdiction)**
>     - [ ] 中国大陆 (Mainland China)
>     - [ ] 中国香港 (Hong Kong) / 澳门 (Macau)
>     - [ ] 涉外/跨境 (Cross-border) - 请注明具体国家/法域
>     - [ ] 不限 (General Theory/Comparative Law)
> 2.  **研究性质/目标 (Research Nature)**
>     - [ ] **实务解决 (Practical Solution)**: 针对具体案件寻找裁判规则或实操指引。
>     - [ ] **合规咨询 (Compliance)**: 排查业务模式的法律风险点。
>     - [ ] **理论研究 (Academic)**: 撰写论文或深度文章，需要学理观点。
>     - [ ] **法条溯源 (Statutory)**: 寻找特定法条的立法本意、沿革或解释。
> 3.  **角色定位 (Role Context)**
>     - [ ] **原告/申请人代理人**: 寻找支持我方诉求的依据。
>     - [ ] **被告/被申请人代理人**: 寻找抗辩理由和相反案例。
>     - [ ] **中立/裁判者**: 需要全面、客观的法律适用分析。
>     - [ ] **企业法务**: 侧重于风险预防和商业可行性。
> 4.  **期望产出格式 (Output Format)**
>     - [ ] **研究备忘录 (Legal Memo)**: 标准法律文书格式，包含问题、结论、分析。
>     - [ ] **案例列表 (Case List)**: 仅提供类案检索报告（支持/反对观点分组）。
>     - [ ] **简报/摘要 (Executive Summary)**: 短篇幅的核心观点提炼。
>     - [ ] **法规汇编 (Statute Compilation)**: 相关法律法规的结构化罗列。

## 检索策略 (Search Strategy)

系统将根据上述回答调整检索权重：

- **若选“实务解决”**: 优先检索“指导性案例”、“公报案例”及本省高院判例；注重“裁判要旨”。
- **若选“合规咨询”**: 优先检索行政处罚案例、监管部门答复 (Q&A)、合规指引。
- **若选“理论研究”**: 增加对核心期刊论文、法学专家观点的检索权重。

## 输出结构示例 (Output Structure)

### 法律备忘录 (Demo)

1.  **问题呈现 (Issues Presented)**
2.  **简要结论 (Short Answer)**
3.  **详细分析 (Discussion)**
    - _法律依据 (Authorities)_: 法条 + 司法解释
    - _案例分析 (Case Analysis)_: 类似情形下的法院观点
    - _适用讨论 (Application)_: 将规则应用到本案事实
4.  **建议与行动 (Recommendations)**

## 免责声明 (Disclaimer)

AI 检索结果可能存在滞后或遗漏，不保证覆盖所有最新生效的法律法规。仅供专业人士作为研究线索参考。
