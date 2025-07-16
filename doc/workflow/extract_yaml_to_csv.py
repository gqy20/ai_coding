#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取工作流文件YAML信息到CSV
简单脚本，无需命令行参数
"""

import os
import csv
import re
from pathlib import Path

def extract_yaml_from_md(file_path):
    """从markdown文件中提取YAML frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 匹配YAML frontmatter (---开头和结尾)
        yaml_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
        if not yaml_match:
            return None
        
        yaml_content = yaml_match.group(1)
        
        # 简单解析YAML（避免依赖外部库）
        yaml_data = {}
        current_key = None
        in_list = False
        list_items = []
        
        for line in yaml_content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # 处理键值对
            if ':' in line and not line.startswith('-'):
                if in_list and current_key:
                    yaml_data[current_key] = ', '.join(list_items)
                    list_items = []
                    in_list = False
                
                key, value = line.split(':', 1)
                key = key.strip().strip('"')
                value = value.strip().strip('"')
                
                if value:  # 单行值
                    yaml_data[key] = value
                    current_key = None
                else:  # 多行值（列表）
                    current_key = key
                    in_list = True
            
            # 处理列表项
            elif line.startswith('-') and current_key:
                item = line[1:].strip().strip('"')
                if item:
                    list_items.append(item)
        
        # 处理最后的列表
        if in_list and current_key:
            yaml_data[current_key] = ', '.join(list_items)
        
        return yaml_data
    
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return None

def main():
    """主函数"""
    # 当前目录（workflow文件夹）
    current_dir = Path(__file__).parent
    
    # 查找所有.md文件
    md_files = list(current_dir.glob('*.md'))
    
    if not md_files:
        print("未找到markdown文件")
        return
    
    # 收集所有YAML数据
    all_data = []
    all_keys = set()
    
    for md_file in md_files:
        print(f"处理文件: {md_file.name}")
        yaml_data = extract_yaml_from_md(md_file)
        
        if yaml_data:
            yaml_data['filename'] = md_file.name  # 添加文件名
            all_data.append(yaml_data)
            all_keys.update(yaml_data.keys())
        else:
            print(f"  → 未找到YAML frontmatter")
    
    if not all_data:
        print("未找到任何YAML数据")
        return
    
    # 确定CSV列顺序（重要字段在前）
    priority_keys = ['filename', 'title', 'version', 'author', 'category', 'description']
    other_keys = sorted([k for k in all_keys if k not in priority_keys])
    csv_columns = [k for k in priority_keys if k in all_keys] + other_keys
    
    # 写入CSV文件
    csv_file = current_dir / 'workflow_metadata.csv'
    
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            
            for data in all_data:
                # 确保所有列都有值（空值用空字符串）
                row = {col: data.get(col, '') for col in csv_columns}
                writer.writerow(row)
        
        print(f"\n✅ 成功生成CSV文件: {csv_file}")
        print(f"📊 处理了 {len(all_data)} 个文件")
        print(f"📋 包含 {len(csv_columns)} 个字段")
        
        # 显示字段列表
        print(f"\n字段列表:")
        for i, col in enumerate(csv_columns, 1):
            print(f"  {i:2d}. {col}")
    
    except Exception as e:
        print(f"写入CSV文件时出错: {e}")

if __name__ == "__main__":
    main()
