# prompt for semantic extraction from LLM
prompt_template = """
You are an expert in program analysis and semantic understanding.
Your task is to analyze the given source code and its Abstract Syntax Tree (AST) to extract **semantic relationships** 
and generate **node-level annotations** that reflect the deep logical and semantic structure of the code.

### TASK OBJECTIVES
1. Understand the logic, data flow, and control flow of the code.
2. Identify key execution paths, semantic dependencies, and relationships between code elements.
3. Output all **semantic relationships** as structured triples in the form of (subject, relation, object).
4. For each AST node, provide a semantic comment, describing its meaning and function.

### INPUT FORMAT
[Source Code]
{source_code}

[Abstract Syntax Tree (AST)]
{ast_text}

### OUTPUT FORMAT

Please output strictly in the following structure:

#### 1. Semantic Relations
List all semantic relationships as triples in the form:
(subject, relation, object)
Example:
(function_foo, defines, variable_a)
(variable_a, compared_with, variable_b)

#### 2. Node Comments
For each AST node, provide a short and meaningful comment (10–20 characters), 
clearly describing its semantic role and function in the code.

#### 3. JSON Structure
If possible, also provide a JSON representation of the results in the following format:
{{
  "semantic_relations": [
    ["subject1", "relation1", "object1"],
    ["subject2", "relation2", "object2"]
  ],
  "node_annotations": {{
    "NodeName": "comment"
  }}
}}

### INSTRUCTIONS
- The relationships should capture both **control flow** (e.g., controls, calls, returns_to) 
  and **data dependencies** (e.g., defines, uses, assigns, compares).
- Summaries must reflect the intent and logic of the code, not just syntax.
- Avoid including irrelevant or redundant details.
- Respond **only** with the requested structured outputs — no extra explanations.
"""
