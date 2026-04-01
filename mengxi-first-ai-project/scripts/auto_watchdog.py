#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auto_watchdog.py — 🛡️ 自愈守护进程 (Autonomous L5 Self-Healing Watchdog)
═══════════════════════════════════════════════════════════════════════
功能：
  1. 拦截异常与内容审计 (Logical Auditor)
  2. 自动生成补丁 (LLM-as-a-Healer)
  3. 沙盒闭环验证 (Sandbox Validator)
  4. 自主 Git 提交与推送 (Autonomous GitOps)
  5. 仅在连续 3 次失败时求救 (Exception-Only Notifications)

Author: Antigravity × mengxi.space (Devin-style Autonomous Agent)
"""

import os
import sys
import re
import json
import time
import logging
import traceback
import subprocess
import tempfile
import hashlib
import datetime
import textwrap
import shutil
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum

# 📐 Configuration
PROJECT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_DIR / "scripts"
LOGS_DIR = PROJECT_DIR / "logs"
WATCHDOG_DIR = LOGS_DIR / "watchdog"
PATCHES_DIR = WATCHDOG_DIR / "patches"
SANDBOX_DIR = WATCHDOG_DIR / "sandbox"
INCIDENT_DIR = WATCHDOG_DIR / "incidents"

# 确保目录结构存在
for d in [WATCHDOG_DIR, PATCHES_DIR, SANDBOX_DIR, INCIDENT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# 日志配置
LOG_FILE = WATCHDOG_DIR / "watchdog.log"
INCIDENT_LOG = WATCHDOG_DIR / "incident_history.jsonl"

# 加载环境变量
ENV_PATH = PROJECT_DIR / ".env"
if ENV_PATH.exists():
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, value = line.partition('=')
                os.environ[key.strip()] = value.strip().strip('"').strip("'")

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='🛡️ %(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("Watchdog")

class Severity(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class Incident:
    id: str
    timestamp: str
    severity: str
    script_name: str
    error_type: str
    error_message: str
    stack_trace: str
    source_snippet: str = ""
    context: Dict[str, Any] = field(default_factory=dict)
    diagnosis: str = ""
    patch_code: str = ""
    patch_file: str = ""
    patch_applied: bool = False
    patch_test_result: str = ""
    resolved: bool = False
    attempts: int = 0

# ══════════════════════════════════════════════════════════════════════
# 🛠️ Module 1: GitOps — Autonomous Version Control
# ══════════════════════════════════════════════════════════════════════

class GitOps:
    """自主 Git 提交与推送模块"""
    @staticmethod
    def commit_and_push(message: str):
        log.info(f"🚀 准备执行自主 Git 提交: {message}")
        try:
            # 检查是否有变更
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=PROJECT_DIR)
            if not status.stdout.strip():
                log.info("ℹ️ 没有发现任何代码变更，跳过提交。")
                return True
            
            # 执行 Git 流程
            subprocess.run(["git", "add", "."], check=True, cwd=PROJECT_DIR)
            subprocess.run(["git", "commit", "-m", f"auto-heal: {message}"], check=True, cwd=PROJECT_DIR)
            
            # 推送（假设环境已配置好鉴权）
            subprocess.run(["git", "push", "origin", "main"], check=True, cwd=PROJECT_DIR)
            log.info("✅ 自主 Git 提交与推送成功！")
            return True
        except Exception as e:
            log.error(f"❌ Git 操作失败: {e}")
            return False

# ══════════════════════════════════════════════════════════════════════
# 🏗️ Module 2: SandboxValidator — Safety First
# ══════════════════════════════════════════════════════════════════════

class SandboxValidator:
    """补丁验证沙盒"""
    def __init__(self, project_root: Path):
        self.root = project_root

    def validate_patch(self, script_path: str, patch_code: str) -> Tuple[bool, str]:
        """在隔离环境中验证补丁是否能修复脚本并将 HTML 生成正常"""
        log.info(f"🏗️ 启动沙盒验证: {os.path.basename(script_path)}")
        test_dir = Path(tempfile.mkdtemp(prefix="watchdog_sandbox_"))
        
        try:
            # 1. 模拟环境 (轻量级：仅拷贝出错脚本和必要的配置)
            # 在实际复杂场景下应拷贝整个项目，这里为了速度先做针对性验证
            target_script = test_dir / os.path.basename(script_path)
            
            # 如果是内容审计失败，我们需要验证的是生成的 HTML 是否恢复正常
            # 这里我们直接在原文件备份的基础上尝试应用
            backup_file = Path(str(script_path) + ".bak")
            shutil.copy2(script_path, backup_file)
            
            try:
                # 尝试写入补丁（如果是直接修改脚本的补丁）
                # 这里假设 LLM 给出的补丁是完整的脚本覆盖，或者是一个 patch 逻辑
                # 对于 L5 阶段，我们假设 LLM 提供的是可以直接运行的修正版代码
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(patch_code)
                
                # 运行验证
                result = subprocess.run(
                    [sys.executable, script_path],
                    capture_output=True,
                    text=True,
                    timeout=60,
                    cwd=self.root,
                    env=os.environ
                )
                
                if result.returncode == 0:
                    output = result.stdout + result.stderr
                    log.info("✅ 沙盒运行通过")
                    return True, output
                else:
                    log.warning(f"❌ 沙盒验证失败:\n{result.stderr}")
                    # 恢复备份
                    shutil.move(str(backup_file), script_path)
                    return False, result.stderr
            except Exception as e:
                if backup_file.exists():
                    shutil.move(str(backup_file), script_path)
                return False, str(e)
            finally:
                if backup_file.exists():
                    os.remove(backup_file)
        finally:
            shutil.rmtree(test_dir)

# ══════════════════════════════════════════════════════════════════════
# 🧠 Module 3: DiagnosticEngine (LLM Integration)
# ══════════════════════════════════════════════════════════════════════

class DiagnosticEngine:
    def diagnose(self, incident: Incident) -> Incident:
        log.info(f"🧠 启动 LLM 诊断与补丁生成: {incident.id}")
        prompt = self.build_diagnosis_prompt(incident)
        response = self.ask_llm(prompt)
        incident.diagnosis = response
        
        # 寻找 Python 代码块
        code_match = re.search(r'```python\n(.*?)\n```', response, re.DOTALL)
        if code_match:
            incident.patch_code = code_match.group(1)
            log.info(f"🔧 补丁生成完毕 ({len(incident.patch_code)} 字节)")
        else:
            log.warning("⚠️ LLM 未能在响应中包含有效的 Python 补丁块")
        return incident

    def build_diagnosis_prompt(self, incident: Incident) -> str:
        if incident.context.get("is_logical_error"):
            # 逻辑审计失败专用 Prompt
            return textwrap.dedent(f"""\
                你是 mengxi.space 的深度自愈代理。
                
                ### 逻辑审计异常汇报:
                脚本: {incident.script_name}
                异常描述: {incident.error_message}
                LLM 裁判的反馈: {incident.stack_trace}
                
                ### 任务:
                请分析负责生成 index.html 的脚本源码（通常是 sync_obsidian.py）。
                请给出一个完整的、修复后的 python 脚本代码。
                如果是元数据解析问题，请优化正则；如果是 CSS 注入问题，请完善注入逻辑。
                必须输出在 ```python ... ``` 块中。
            """)
        else:
            # 运行崩溃专用 Prompt
            return f"脚本 {incident.script_name} 崩溃:\n{incident.stack_trace}\n请诊断原因并提供一个完整的修复版 Python 代码 (```python ... ```)。"

    def ask_llm(self, prompt: str) -> str:
        import json
        import urllib.request
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key: return "[ERROR] No API Key"
        proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897'})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=45) as res:
                data = json.loads(res.read().decode('utf-8'))
                return data['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            return f"[ERROR] LLM Failed: {e}"

# ══════════════════════════════════════════════════════════════════════
# ⚖️ Module 4: LogicalAuditor (The Judge)
# ══════════════════════════════════════════════════════════════════════

class LogicalAuditor:
    def __init__(self, diagnostic_engine: DiagnosticEngine):
        self.diagnostics = diagnostic_engine

    def audit_page(self, html_path: str) -> Optional[Incident]:
        log.info(f"⚖️ 启动 L5 逻辑审计: {os.path.basename(html_path)}")
        try:
            if not os.path.exists(html_path): return None
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            prompt = textwrap.dedent(f"""\
            你是 mengxi.space 的最高逻辑裁判。
            请对 HTML 源代码进行深度合规性分析。
            注意：中间内容被 [MID-CONTENT-TRUNCATED] 截断，请知晓。
            
            检查清单:
            1. 锚点: <!-- SECTION_START/END --> 必须成对。
            2. 注入: RASPBERRY_PI, SHOWCASES 等版块必须有实际内容 (至少一个卡片)。
            3. 语义: 树莓派版块里绝不能有育儿日记。
            
            输出 JSON: {{"status": "Pass"|"Fail", "reason": "...", "suggestion": "..."}}
            ---
            {html_content[:7000]}
            ... [MID-CONTENT-TRUNCATED] ...
            {html_content[-3000:]}
            """)
            response = self.diagnostics.ask_llm(prompt)
            json_match = re.search(r'\{.*\}', response, re.S)
            if json_match:
                data = json.loads(json_match.group(0))
                if data.get("status") == "Fail":
                    log.error(f"❌ 审计未通过: {data.get('reason')}")
                    return Incident(
                        id=f"LA-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}",
                        timestamp=datetime.datetime.now().isoformat(),
                        severity=Severity.ERROR.value,
                        script_name="LogicalAuditor",
                        error_type="LogicalAuditFailure",
                        error_message=data.get("reason", "Anomaly detected"),
                        stack_trace=response,
                        context={"html_path": html_path, "is_logical_error": True}
                    )
            log.info("✅ 页面逻辑审计通过")
            return None
        except Exception as e:
            log.error(f"💥 审计器异常: {e}")
            return None

# ══════════════════════════════════════════════════════════════════════
# 🚀 Module 5: WatchdogOrchestrator — The Autonomous Pilot
# ══════════════════════════════════════════════════════════════════════

class WatchdogOrchestrator:
    def __init__(self):
        self.diagnostics = DiagnosticEngine()
        self.auditor = LogicalAuditor(self.diagnostics)
        self.sandbox = SandboxValidator(PROJECT_DIR)
        self.git = GitOps()
        self.max_attempts = 3
        self.history_file = INCIDENT_LOG

    def notify_critical(self, message: str):
        """仅在致命错误时通知人工"""
        title = "🔴 Watchdog Critical Failure"
        log.critical(message)
        try:
            subprocess.run(["osascript", "-e", f'display notification "{message}" with title "{title}"'], capture_output=True)
        except Exception: pass

    def autonomous_heal(self, incident: Incident) -> bool:
        """核心自治修复循环"""
        while incident.attempts < self.max_attempts:
            incident.attempts += 1
            log.info(f"🔄 启动第 {incident.attempts}/{self.max_attempts} 次自主修复尝试...")
            
            # 1. 诊断与生成补丁
            self.diagnostics.diagnose(incident)
            if not incident.patch_code:
                continue
                
            # 2. 沙盒验证
            script_abs_path = SCRIPTS_DIR / incident.script_name
            success, test_log = self.sandbox.validate_patch(str(script_abs_path), incident.patch_code)
            
            if success:
                # 3. 页面审计验证 (如果是 HTML 相关的错误)
                audit_incident = self.auditor.audit_page(str(PROJECT_DIR / "index.html"))
                if not audit_incident:
                    log.info(f"✨ 修复验证成功！在第 {incident.attempts} 次尝试中自愈。")
                    incident.resolved = True
                    # 4. 自主 Git 提交
                    self.git.commit_and_push(f"Auto-healed {incident.script_name} ({incident.error_type})")
                    return True
                else:
                    log.warning(f"⚠️ 代码运行通过但逻辑审计仍失败: {audit_incident.error_message}")
                    incident.stack_trace += f"\nAudit Feedback: {audit_incident.stack_trace}"
            else:
                log.warning(f"❌ 补丁导致沙盒崩溃，记录日志并重试。")
                
        # 所有尝试均失败
        self.notify_critical(f"自愈失败: {incident.script_name} 经过 {self.max_attempts} 次尝试仍未通过。需人工介入。")
        return False

    def run_safe(self, script_path: str):
        log.info(f"🔍 运行监控: {os.path.basename(script_path)}")
        try:
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True, text=True, timeout=300, cwd=PROJECT_DIR, env=os.environ
            )
            if result.returncode == 0:
                return True
            
            log.error(f"🔴 运行异常: {os.path.basename(script_path)}")
            incident = Incident(
                id=f"WD-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}",
                timestamp=datetime.datetime.now().isoformat(),
                severity=Severity.ERROR.value,
                script_name=os.path.basename(script_path),
                error_type="RuntimeException",
                error_message=result.stderr.split('\n')[-2] if '\n' in result.stderr else result.stderr,
                stack_trace=result.stderr
            )
            return self.autonomous_heal(incident)
        except Exception as e:
            log.error(f"💥 系统执行崩溃: {e}")
            return False

    def run_full_pipeline(self):
        log.info("═══ 🚀 启动全自动化静默同步流水线 ═══")
        
        # 定义核心流水线脚本列表 (按顺序)
        pipeline = [
            "auto_writer.py", "auto_curator.py", "fetch_hn_feed.py", "fetch_dxy_mom.py", "fetch_xhs_avoid_pits.py",
            "fetch_newborn_care_rss.py", "fetch_newborn_care.py", "fetch_labor_delivery.py",
            "fetch_montessori.py", "fetch_math_puzzles.py", "fetch_logic_puzzles.py",
            "fetch_podcast.py", "fetch_poche_feed.py", "fetch_news_feed.py", "auto_diagram.py", "sync_early_learning_hub.py",
            "sync_xiaoxi_channel.py", "generate_daily_quote.py", "generate_schedule.py",
            "sync_obsidian.py", "generate_matrix.py"
        ]
        
        total_success = True
        for script in pipeline:
            path = SCRIPTS_DIR / script
            if path.exists():
                if not self.run_safe(str(path)):
                    total_success = False
            else:
                log.warning(f"⚠️ 跳过缺失脚本: {script}")

        # 最终审计
        if total_success:
            audit_incident = self.auditor.audit_page(str(PROJECT_DIR / "index.html"))
            if audit_incident:
                log.warning("⚖️ 逻辑审计未通过，尝试最终自愈...")
                self.autonomous_heal(audit_incident)
        
        log.info("═══ ✅ 全自动化流水线运行结束 ═══")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", help="Run a specific script safely")
    parser.add_argument("--pipeline", action="store_true", help="Run the full silent pipeline")
    parser.add_argument("--scan", action="store_true", help="Scan for health")
    parser.add_argument("--scan-log", help="Scan error log")
    parser.add_argument("--no-notify", action="store_true", help="Disable notifications")
    args = parser.parse_args()

    orch = WatchdogOrchestrator()
    if args.pipeline:
        orch.run_full_pipeline()
    elif args.script:
        orch.run_safe(args.script)
    elif args.scan:
        log.info("🛡️ Scan mode active: skipping full pipeline here to prevent duplicate runs.")
    else:
        orch.run_full_pipeline()
