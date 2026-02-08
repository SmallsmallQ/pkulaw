# 智能合同审查 (Review)

该指令用于依据特定的法律框架和企业内部风控政策（Playbook），对合同或其他法律文件进行全面、自动化的审查。系统将识别潜在风险，并支持**批注模式**直接在 Word/PDF 文档中生成修改建议。

## 核心功能 (Core Capabilities)

- **多维合规扫描**：覆盖个人信息保护、广告合规、反垄断等专项领域。
- **智能批注 (Smart Annotation)**：支持在 Word 中插入批注 (Comments) 或修订 (Track Changes)，以及 PDF 高亮批注。
- **红线比对 (Redline)**：生成便于修订的对比版本。

## 使用方法 (Usage)

```bash
/review [File] [--criterion <standard>] [--mode <output_mode>]
```

### 参数说明 (Input Parameters)

| 参数          | 说明                                                                       | 默认值     |
| :------------ | :------------------------------------------------------------------------- | :--------- |
| `File`        | 待审查的 Word (.docx) 或 PDF 文件路径                                      | -          |
| `--criterion` | 审查标准：`standard` (通用), `buyer`, `seller`, `pipl` (个保), `ad` (广告) | `standard` |
| `--mode`      | **输出模式** (见下文详情)                                                  | `report`   |

### 输出模式 (Output Modes)

- `report`: 生成 Markdown 格式的风险评估报告（默认）。
- `redline`: 生成带有“修订模式” (Track Changes) 的 Word 文档，直接展示增删操作。
- `comment`: **[NEW]** 在 Word 文档侧边栏添加**批注 (Comments)**，提出修改建议和风险提示，不修改原文。
- `pdf-mark`: **[NEW]** 将文档转换为 PDF（如原文件为 Word），并在对应位置添加**高亮和旁注 (Sticky Notes)**。

## 审查维度 (Review Dimensions)

### 1. 通用法律审查 (General Legal)

- **合法性 (Legality)**：检查违反《民法典》强制性规定的条款（如格式条款效力）。
- **权益平衡 (Equity)**：识别“显失公平”或过度单边保护的条款。

### 2. 专项合规审查 (Special Compliance)

> 需配合 `compliance-check` 技能库

- **个人信息保护 (PIPL)**
  - 检查隐私政策、DPA 等文件。
  - **审查点**：是否明示处理目的？是否取得单独同意？是否存在过度收集？
- **广告合规 (Advertising)**
  - 检查营销文案、合同中的宣传条款。
  - **审查点**：绝对化用语（“第一”、“顶级”）、虚假宣传风险。
- **反垄断与竞争 (Antimonopoly)**
  - 检查经销协议、排他协议。
  - **审查点**：固定转售价格 (RPM)、“二选一”限制条款。

### 3. 商业风控 (Commercial Risk)

- **交易条款**：付款账期 (Payment Terms)、违约金比例 (Liquidated Damages)、不可抗力。
- **知识产权**：IP 归属与授权范围。

## 批注模式工作流 (Annotation Workflow)

### Word 批注模式 (`--mode comment`)

系统不修改文档正文，而是以**审阅者**身份添加批注：

- **选中相关条款**：精准定位风险语句。
- **批注内容**：
  - 🔴 **[High]** 风险描述 + 修改建议。
  - 🟡 **[Medium]** 谈判提示。
- **适用场景**：法务初审，需保留原文供业务部门决策。
- **执行指令**：
  ```bash
  ./pkulaw-plugins/venv/bin/python pkulaw-plugins/scripts/docx_annotator.py "{file_path}" "{target_text}" "{comment_text}" --author "AI Reviewer"
  ```

### PDF 批注模式 (`--mode pdf-mark`)

系统生成 PDF 副本并进行标注：

- **高亮 (Highlight)**：黄色高亮风险条款。
- **旁注 (Sticky Note)**：点击高亮处显示详细合规建议。
- **适用场景**：向外部发送不可编辑的审阅意见，或归档存证。

## 免责声明 (Disclaimer)

AI 审查结果仅供参考，不能完全替代人工审查。特别是对于复杂的合规场景（如跨国数据传输、反垄断界定），建议咨询专业律师。
