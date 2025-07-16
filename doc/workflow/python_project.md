# Python项目开发工作流 - AI助手指南

## 1. 概述

这是一个专门为AI助手设计的Python项目开发工作流，提供从需求分析到项目交付的完整指导思路。使用 uv 作为现代Python包管理器，确保开发环境的快速和可靠。

## 2. 核心开发思路

### 2.1 开发流程
```
需求分析 → 技术选型 → 项目结构 → 核心开发 → 测试优化 → 文档交付
```

### 2.2 技术栈选择

#### 2.2.1 项目类型识别
- **Web API**: 包含 "api", "web", "服务", "接口" 关键词 → Flask/FastAPI
- **数据处理**: 包含 "数据", "分析", "csv", "excel" 关键词 → Pandas
- **命令行工具**: 包含 "cli", "命令行", "工具", "脚本" 关键词 → Click
- **桌面应用**: 包含 "gui", "桌面", "界面" 关键词 → Tkinter

#### 2.2.2 框架选择逻辑
- **Flask**: 轻量级Web开发，适合简单API
- **FastAPI**: 现代异步API，支持自动文档生成
- **Pandas**: 数据处理和分析
- **Click**: 命令行工具开发

## 3. 项目实现步骤

### 3.1 环境准备

#### 3.1.1 安装 uv
```bash
# Windows
curl -LsSf https://astral.sh/uv/install.ps1 | powershell

# Linux/macOS  
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 3.1.2 创建项目
```bash
mkdir project_name
cd project_name
uv init
```

### 3.2 项目结构

#### 3.2.1 标准结构
```
project_name/
├── src/
│   ├── __init__.py
│   ├── main.py          # 主入口
│   ├── models.py        # 数据模型
│   ├── utils.py         # 工具函数
│   └── config.py        # 配置文件
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml       # uv项目配置
├── .env.example         # 环境变量示例
└── README.md
```

### 3.3 依赖管理

#### 3.3.1 添加依赖
```bash
# Web API
uv add flask flask-sqlalchemy

# 数据处理
uv add pandas numpy matplotlib

# 命令行工具
uv add click

# 开发依赖
uv add --dev pytest black
```

#### 3.3.2 虚拟环境
```bash
# 激活环境
uv venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 安装依赖
uv sync
```

## 4. 代码规范

### 4.1 基本规范

#### 4.1.1 类型提示
```python
def process_data(items: list[dict], rate: float = 0.1) -> dict:
    """处理数据并返回结果"""
    result = {"count": len(items), "rate": rate}
    return result
```

#### 4.1.2 错误处理
```python
def safe_operation(data: str) -> str | None:
    try:
        return data.upper()
    except AttributeError:
        return None
```

#### 4.1.3 配置管理
```python
# config.py
import os
from dataclasses import dataclass

@dataclass
class Config:
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///app.db")
```

### 4.2 项目类型模板

#### 4.2.1 Web API (Flask)
```python
# main.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': '缺少姓名'}), 400
    
    # 业务逻辑
    user = {'id': 1, 'name': data['name']}
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)
```

#### 4.2.2 数据处理工具
```python
# main.py
import pandas as pd
from pathlib import Path

def process_csv(input_file: str, output_file: str) -> None:
    """处理CSV文件"""
    df = pd.read_csv(input_file)
    
    # 数据清洗
    df = df.dropna()
    df = df.drop_duplicates()
    
    # 保存结果
    df.to_csv(output_file, index=False)
    print(f"处理完成: {len(df)} 行数据")

if __name__ == '__main__':
    process_csv('input.csv', 'output.csv')
```

#### 4.2.3 命令行工具
```python
# main.py
import click

@click.command()
@click.option('--input', '-i', required=True, help='输入文件')
@click.option('--output', '-o', default='output.txt', help='输出文件')
def process(input_file: str, output: str) -> None:
    """文件处理工具"""
    with open(input_file, 'r') as f:
        content = f.read().upper()
    
    with open(output, 'w') as f:
        f.write(content)
    
    click.echo(f"处理完成: {output}")

if __name__ == '__main__':
    process()
```

## 5. 测试策略

### 5.1 单元测试

#### 5.1.1 测试配置
```bash
uv add --dev pytest pytest-cov
```

#### 5.1.2 测试示例
```python
# tests/test_main.py
import pytest
from src.main import process_data

def test_process_data():
    items = [{'price': 100}, {'price': 200}]
    result = process_data(items, 0.1)
    
    assert result['count'] == 2
    assert result['rate'] == 0.1

def test_process_data_empty():
    result = process_data([], 0.1)
    assert result['count'] == 0
```

#### 5.1.3 运行测试
```bash
uv run pytest
uv run pytest --cov=src  # 覆盖率报告
```

## 6. 项目配置文件

### 6.1 pyproject.toml 配置
```toml
[project]
name = "project-name"
version = "0.1.0"
description = "项目描述"
authors = [{name = "AI Assistant", email = "ai@example.com"}]
requires-python = ">=3.8"
dependencies = [
    "flask>=2.3.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.ruff]
line-length = 88
target-version = "py38"
```

### 6.2 环境变量配置
```bash
# .env.example
DEBUG=true
DATABASE_URL=sqlite:///app.db
SECRET_KEY=your-secret-key
API_PORT=5000
```

## 7. 部署运行

### 7.1 开发环境运行
```bash
# 激活环境并安装依赖
uv sync

# 运行项目
uv run python src/main.py

# 运行测试
uv run pytest
```

### 7.2 生产环境部署
```bash
# 构建项目
uv build

# 安装到生产环境
uv pip install dist/*.whl
```

## 8. 质量检查清单

### 8.1 开发完成检查
- [ ] 代码使用类型提示
- [ ] 函数有文档字符串
- [ ] 错误处理完善
- [ ] 测试覆盖率 > 80%
- [ ] 所有功能正常运行

### 8.2 文档完成检查
- [ ] README.md 包含安装说明
- [ ] README.md 包含使用示例
- [ ] 代码注释清晰
- [ ] 配置文件有示例

## 9. 自动化脚本

### 9.1 需求分析函数
```python
def analyze_requirement(requirement: str) -> dict:
    """分析用户需求并返回项目配置"""
    import re
    
    # 项目类型检测
    if any(word in requirement.lower() for word in ['api', 'web', 'flask']):
        project_type = 'web_api'
        framework = 'flask'
    elif any(word in requirement.lower() for word in ['数据', 'csv', 'pandas']):
        project_type = 'data_tool'
        framework = 'pandas'
    elif any(word in requirement.lower() for word in ['cli', '命令行', 'click']):
        project_type = 'cli_tool'
        framework = 'click'
    else:
        project_type = 'web_api'
        framework = 'flask'
    
    # 提取项目名称
    name_pattern = r'(?:创建|开发|实现).*?([^\s，。]+(?:系统|工具|API|服务|应用))'
    match = re.search(name_pattern, requirement)
    name = match.group(1) if match else 'python-project'
    
    return {
        'name': name,
        'type': project_type,
        'framework': framework,
        'description': requirement[:100]
    }
```

### 9.2 项目生成函数
```python
def generate_project(config: dict) -> None:
    """根据配置生成项目文件"""
    import os
    
    # 创建目录结构
    os.makedirs(f"{config['name']}/src", exist_ok=True)
    os.makedirs(f"{config['name']}/tests", exist_ok=True)
    
    # 生成主文件
    if config['type'] == 'web_api':
        main_content = '''from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
'''
    elif config['type'] == 'data_tool':
        main_content = '''import pandas as pd

def process_data(file_path: str) -> None:
    df = pd.read_csv(file_path)
    print(f"数据形状: {df.shape}")
    
if __name__ == '__main__':
    process_data('data.csv')
'''
    else:
        main_content = '''import click

@click.command()
@click.option('--name', help='名称')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
'''
    
    # 写入文件
    with open(f"{config['name']}/src/main.py", 'w', encoding='utf-8') as f:
        f.write(main_content)
    
    print(f"项目 {config['name']} 生成完成!")
```

## 10. 使用示例

### 10.1 快速开始
```python
# 使用工作流的完整示例
requirement = "创建一个用户管理API，使用Flask框架，实现用户增删改查功能"

# 1. 分析需求
config = analyze_requirement(requirement)
print(f"项目类型: {config['type']}")
print(f"使用框架: {config['framework']}")

# 2. 生成项目
generate_project(config)

# 3. 进入项目目录，初始化uv环境
# cd user-management-api
# uv init
# uv add flask flask-sqlalchemy
# uv sync
# uv run python src/main.py
```

### 10.2 完整工作流
```bash
# 1. 创建项目
mkdir my-project && cd my-project
uv init

# 2. 添加依赖
uv add flask  # 根据项目类型选择

# 3. 开发代码
# 编写 src/main.py

# 4. 添加测试
uv add --dev pytest
# 编写 tests/test_main.py

# 5. 运行和测试
uv run python src/main.py
uv run pytest

# 6. 代码格式化
uv add --dev black
uv run black src/
```

---

**工作流版本**: v2.0  
**更新日期**: 2025-07-16  
**适用于**: Python 3.8+ with uv package manager
