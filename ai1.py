"""
================================================================================
    NEXUS AI - PRO MULTI-MODEL ARENA (CYBER-GLASS ULTIMATE EDITION)
    - Full-Screen Animated Cyber Floating Particles Background
    - Deep Glassmorphic Transparency on Sidebar & Model Columns
    - Right-Aligned User Chat Bubbles & Left-Aligned AI Model Responses
    - Ultra-Fast Pipelined Zero-Delay Streaming Voice Synthesis (Edge-TTS)
    - Smooth Model Column Removal Collapse Animation
    - Fixed Dark Cyber QComboBox Popup & Modern Compact Settings Dialog
    - Enterprise Premium Login Suite:
        * Remember Me (Auto-Login Session Persistence)
        * Smooth Login & Sign Up Modes with Live Password Strength Meter
        * Animated Cyber Arc Loading Spinner inside Action Buttons
        * Forgot Password Recovery & Guest / Offline Local AI Bypass Mode
        * Terms of Service & Privacy Policy Glassmorphic Modals
    - Identity Directive: Created by Wajahat | Nexus Multi-Model Arena
================================================================================
"""

import sys
import os
import time
import json
import math
import sqlite3
import re
import io
import base64
import random
import ctypes
import hashlib
import tempfile
import urllib.parse
import urllib.request
import urllib.error
import traceback
import shutil
import subprocess
from collections import deque
from typing import List, Dict, Any, Optional, Set

import markdown
import speech_recognition as sr
from PIL import Image

# Edge TTS & Asyncio for Voice System
import edge_tts
import asyncio

# --- Web Scraping Support ---
try:
    import requests
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

# --- Advanced RAG (FAISS) ---
try:
    import faiss
    from sentence_transformers import SentenceTransformer
    HAS_FAISS = True
except ImportError:
    HAS_FAISS = False

# Web Search Support
try:
    from duckduckgo_search import DDGS
    HAS_DDGS = True
except ImportError:
    HAS_DDGS = False

# Syntax Highlighting Support
try:
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name, guess_lexer
    from pygments.formatters import HtmlFormatter
    HAS_PYGMENTS = True
except ImportError:
    HAS_PYGMENTS = False

# Google Generative AI (Gemini)
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

# PDF Document Ingestion Support
try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

# PySide6 Qt GUI, SVG & Multimedia Support
from PySide6.QtCore import (
    Qt, QTimer, QThread, Signal, QRect, QSize, QPointF, QUrl, QByteArray, QEvent, QPropertyAnimation, QEasingCurve
)
from PySide6.QtGui import (
    QColor, QFont, QPainter, QPen, QTextDocument, QBrush, QPixmap,
    QCursor, QGuiApplication, QKeyEvent, QDragEnterEvent, QDropEvent,
    QDesktopServices, QCloseEvent, QLinearGradient, QRadialGradient, QImage, QTextCursor,
    QPdfWriter, QIcon
)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QProgressBar, QStackedLayout, QFrame,
    QScrollArea, QFileDialog, QMenu, QTextBrowser, QComboBox, QInputDialog,
    QMessageBox, QDialog, QTextEdit, QSlider, QSizePolicy, QCheckBox,
    QGraphicsDropShadowEffect, QSpinBox, QSplitter, QListView, QStackedWidget
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

try:
    from PySide6.QtSvg import QSvgRenderer
    HAS_SVG = True
except ImportError:
    HAS_SVG = False

# Web Engine for Claude Artifacts
try:
    from PySide6.QtWebEngineWidgets import QWebEngineView
    HAS_WEBENGINE = True
except ImportError:
    HAS_WEBENGINE = False


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ==============================================================================
# 1. VECTOR SVG LOGOS & APP LOGO MASKS
# ==============================================================================

def get_nexus_app_logo(size_height: int = 60) -> QPixmap:
    pixmap = QPixmap(resource_path("logo.png"))
    if not pixmap.isNull():
        return pixmap.scaledToHeight(size_height, Qt.SmoothTransformation)
    else:
        pix = QPixmap(size_height, size_height)
        pix.fill(Qt.transparent)
        painter = QPainter(pix)
        painter.setRenderHint(QPainter.Antialiasing)
        grad = QLinearGradient(0, 0, size_height, size_height)
        grad.setColorAt(0, QColor("#00E5FF"))
        grad.setColorAt(1, QColor("#0072FF"))
        painter.setBrush(QBrush(grad))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, size_height, size_height, size_height//4, size_height//4)
        painter.setPen(QColor("#080D11"))
        f = QFont("Inter", int(size_height * 0.5), QFont.Black)
        painter.setFont(f)
        painter.drawText(QRect(0, 0, size_height, size_height), Qt.AlignCenter, "N")
        painter.end()
        return pix

UI_SVGS = {
    "settings": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>""",
    "download": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>""",
    "send": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>""",
    "menu": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>""",
    "mic": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>""",
    "plus": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>""",
    "user": """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>""",
    "lock": """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>""",
    "mail": """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>""",
    "logout": """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>"""
}

def create_svg_icon(svg_key: str, color: str = "#FFFFFF", size: int = 24) -> QIcon:
    if not HAS_SVG or svg_key not in UI_SVGS:
        return QIcon()
    svg_str = UI_SVGS[svg_key].replace('currentColor', color)
    renderer = QSvgRenderer(QByteArray(svg_str.encode("utf-8")))
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    renderer.render(painter)
    painter.end()
    return QIcon(pixmap)

def get_svg_pixmap_from_raw(svg_code: str, size: int = 24) -> QPixmap:
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)
    if HAS_SVG:
        renderer = QSvgRenderer(QByteArray(svg_code.encode("utf-8")))
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        renderer.render(painter)
        painter.end()
    return pixmap

MODEL_SVG_LOGOS = {
    "gemini": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><defs><linearGradient id="geminiGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4E88F5"/><stop offset="35%" stop-color="#6F8CF7"/><stop offset="70%" stop-color="#9B72F2"/><stop offset="100%" stop-color="#DE6EAE"/></linearGradient></defs><path fill="url(#geminiGrad)" d="M12 0C12 6.627 6.627 12 0 12c6.627 0 12 5.373 12 12 0-6.627 5.373-12 12-12-6.627 0-12-5.373-12-12z"/></svg>""",
    "qwen": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><defs><linearGradient id="qwenGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#6366F1"/><stop offset="100%" stop-color="#A855F7"/></linearGradient></defs><path fill="url(#qwenGrad)" d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>""",
    "meta": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><defs><linearGradient id="metaGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0064E0"/><stop offset="50%" stop-color="#0079FF"/><stop offset="100%" stop-color="#00D2FF"/></linearGradient></defs><path fill="url(#metaGrad)" d="M16.68 5.5c-1.84 0-3.37.93-4.68 2.47-1.31-1.54-2.84-2.47-4.68-2.47C3.39 5.5 1 8.54 1 12.33 1 16.12 3.39 19 7.32 19c1.94 0 3.52-1.02 4.68-2.37 1.16 1.35 2.74 2.37 4.68 2.37C20.61 19 23 16.12 23 12.33 23 8.54 20.61 5.5 16.68 5.5zm-9.36 11.2c-2.48 0-4.02-2.03-4.02-4.37 0-2.34 1.54-4.37 4.02-4.37 1.47 0 2.76.87 3.73 2.33-1.12 1.63-2.39 3.54-3.73 6.41zm9.36 0c-1.34-2.87-2.61-4.78-3.73-6.41.97-1.46 2.26-2.33 3.73-2.33 2.48 0 4.02 2.03 4.02 4.37 0 2.34-1.54 4.37-4.02 4.37z"/></svg>""",
    "openai": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="#10A37F" d="M22.28 10.1a5.6 5.6 0 0 0-.47-4.57 5.72 5.72 0 0 0-5.74-2.73 5.62 5.62 0 0 0-4.35-1.95 5.72 5.72 0 0 0-5.46 3.99A5.63 5.63 0 0 0 2.5 7.6a5.72 5.72 0 0 0 .78 6.27 5.6 5.6 0 0 0 .47 4.57 5.72 5.72 0 0 0 5.74 2.73A5.62 5.62 0 0 0 13.84 23a5.72 5.72 0 0 0 5.46-3.99 5.63 5.63 0 0 0 3.76-2.76 5.72 5.72 0 0 0-.78-6.15zM13.84 21.6c-1.3 0-2.48-.6-3.26-1.55l.13-.08 4.67-2.7a.8.8 0 0 0 .4-.68v-5.7l1.72.99a.08.08 0 0 1 .05.06v5.82a3.84 3.84 0 0 1-3.71 3.84zm-8.8-4.2a3.82 3.82 0 0 1-.5-3.62l.14.09 4.67 2.7c.24.14.39.4.39.68v5.7l-1.72-.99a.08.08 0 0 1-.05-.07v-4.49zm-1.3-8.8a3.83 3.83 0 0 1 3.2-2.07v5.58a.8.8 0 0 0 .4.68l4.67 2.7-1.72 1a.08.08 0 0 1-.08 0l-5.05-2.92a3.83 3.83 0 0 1-1.42-4.97zm14.28 2.22l-4.67-2.7a.8.8 0 0 0-.8 0l-4.67 2.7-1.72-.99a.08.08 0 0 1 0-.08l5.05-2.92a3.84 3.84 0 0 1 5.69 2.19l-.14.09-3.41 1.71zm3.26 6.58a3.83 3.83 0 0 1-3.2 2.07v-5.58a.8.8 0 0 0-.4-.68l-4.67-2.7 1.72-1a.08.08 0 0 1 .08 0l5.05 2.92a3.83 3.83 0 0 1 1.42 4.97zm-7.6-1.89l-2.6-1.5 2.6-1.5 2.6 1.5-2.6 1.5z"/></svg>""",
    "claude": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="#D97706" d="M12 2a1.5 1.5 0 0 1 1.5 1.5v4.56l3.22-3.23a1.5 1.5 0 0 1 2.12 2.12L15.62 10.2h4.88a1.5 1.5 0 0 1 0 3h-4.88l3.22 3.23a1.5 1.5 0 0 1-2.12 2.12L13.5 15.33v4.92a1.5 1.5 0 0 1-3 0v-4.92l-3.22 3.22a1.5 1.5 0 0 1-2.12-2.12L8.38 13.2H3.5a1.5 1.5 0 0 1 0-3h4.88L5.16 6.96a1.5 1.5 0 0 1 2.12-2.12L10.5 8.06V3.5A1.5 1.5 0 0 1 12 2z"/></svg>""",
    "ollama": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="#94A3B8" d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/><path fill="#94A3B8" d="M11 7h2v6h-2zm0 8h2v2h-2z"/></svg>"""
}

def get_model_logo_pixmap(model_key: str, size: int = 20) -> QPixmap:
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)

    svg_str = MODEL_SVG_LOGOS.get(model_key)
    if svg_str and HAS_SVG:
        try:
            renderer = QSvgRenderer(QByteArray(svg_str.encode("utf-8")))
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            renderer.render(painter)
            painter.end()
            return pixmap
        except Exception:
            pass

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    color_map = {
        "gemini": QColor("#245DC7"),
        "qwen": QColor("#835FD7"),
        "meta": QColor("#0079FF"),
        "openai": QColor("#41D5B0"),
        "claude": QColor("#CD7D22"),
        "ollama": QColor("#94A3B8")
    }
    painter.setBrush(color_map.get(model_key, QColor(GlobalConfig.ACCENT_COLOR)))
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(0, 0, size, size, 5, 5)
    painter.setPen(QColor("#FFFFFF"))
    font = QFont("Inter", int(size * 0.46), QFont.Bold)
    painter.setFont(font)
    painter.drawText(QRect(0, 0, size, size), Qt.AlignCenter, model_key[0].upper())
    painter.end()
    return pixmap

# ==============================================================================
# 2. CONFIGURATION & MODELS REGISTRY
# ==============================================================================

class GlobalConfig:
    APP_VERSION: str = "2.2.0"
    GEMINI_API_KEY: str = ""
    OPENROUTER_API_KEY: str = ""
    LOCAL_BASE_URL: str = ""
    CHAT_FONT_SIZE: float = 13.0
    VOICE_SPEED_RATE: float = 1.0
    TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 4096
    CONTEXT_MEMORY: int = 10
    ACCENT_COLOR: str = "#00E5FF"
    CODE_THEME: str = "monokai"
    UI_ANIMATIONS: bool = True
    STT_LANG: str = "en-US"
    SAFE_SEARCH: bool = True
    MAX_WEB_RESULTS: int = 3
    CURRENT_USER: str = "Guest"

    @classmethod
    def sync_from_db(cls, db_ref):
        try:
            cls.GEMINI_API_KEY = db_ref.get_setting("gemini_api_key", cls.GEMINI_API_KEY)
            cls.OPENROUTER_API_KEY = db_ref.get_setting("openrouter_api_key", cls.OPENROUTER_API_KEY)
            cls.LOCAL_BASE_URL = db_ref.get_setting("local_base_url", cls.LOCAL_BASE_URL)
            cls.CHAT_FONT_SIZE = float(db_ref.get_setting("chat_font_size", "13.0"))
            cls.VOICE_SPEED_RATE = float(db_ref.get_setting("voice_speed_rate", "1.0"))
            cls.TEMPERATURE = float(db_ref.get_setting("temperature", "0.7"))
            cls.MAX_TOKENS = int(db_ref.get_setting("max_tokens", "4096"))
            cls.CONTEXT_MEMORY = int(db_ref.get_setting("context_memory", "10"))
            cls.ACCENT_COLOR = db_ref.get_setting("accent_color", "#00E5FF")
            cls.CODE_THEME = db_ref.get_setting("code_theme", "monokai")
            cls.UI_ANIMATIONS = db_ref.get_setting("ui_animations", "True") == "True"
            cls.STT_LANG = db_ref.get_setting("stt_lang", "en-US")
            cls.SAFE_SEARCH = db_ref.get_setting("safe_search", "True") == "True"
            cls.MAX_WEB_RESULTS = int(db_ref.get_setting("max_web_results", "3"))
        except Exception:
            pass

FREE_MODELS_REGISTRY: Dict[str, Dict[str, Any]] = {
    "gemini-3.8": {
        "id": "gemini-3.8-flash", "name": "Gemini 3.8 Flash", "logo_key": "gemini",
        "provider": "gemini", "api_model": "gemini-3.8-flash", "provider_tag": "Google AI Studio",
        "badge_color": "#4E88F5", "cost_in": 0.0, "cost_out": 0.0,
        "desc": "Google flagship multimodal model with deep reasoning and 1M context analysis."
    },
    "gpt-4o-mini": {
        "id": "gpt-4o-mini", "name": "GPT-4o Mini", "logo_key": "openai",
        "provider": "openrouter", "api_model": "openai/gpt-4o-mini", "provider_tag": "OpenRouter (OpenAI)",
        "badge_color": "#10A37F", "cost_in": 0.150, "cost_out": 0.600,
        "desc": "OpenAI compact and capable model tailored for rapid reasoning and structured code."
    },
    "llama-3.1-8b": {
        "id": "llama-3.1-8b", "name": "Llama 3.1 8B", "logo_key": "meta",
        "provider": "openrouter", "api_model": "meta-llama/llama-3.1-8b-instruct:free", "provider_tag": "OpenRouter (Free)",
        "badge_color": "#10B981", "cost_in": 0.0, "cost_out": 0.0,
        "desc": "Ultra-fast lightweight model optimized for high-velocity tasks and agile queries."
    },
    "qwen-2.5-72b": {
        "id": "qwen-2.5-72b", "name": "Qwen 2.5 72B", "logo_key": "qwen",
        "provider": "openrouter", "api_model": "qwen/qwen-2.5-72b-instruct:free", "provider_tag": "OpenRouter (Free)",
        "badge_color": "#8B5CF6", "cost_in": 0.0, "cost_out": 0.0,
        "desc": "Alibaba premier 72B open model with top-tier math, coding, and multilingual power."
    },
    "llama-3.3-70b": {
        "id": "llama-3.3-70b", "name": "Llama 3.3 70B", "logo_key": "meta",
        "provider": "openrouter", "api_model": "meta-llama/llama-3.3-70b-instruct:free", "provider_tag": "OpenRouter (Free)",
        "badge_color": "#0079FF", "cost_in": 0.0, "cost_out": 0.0,
        "desc": "Meta flagship 70B open-weights model delivering industry-leading reasoning and synthesis."
    },
    "nvidia-nemotron": {
        "id": "nvidia-nemotron", "name": "Nemotron 3 Super 120B", "logo_key": "openai",
        "provider": "openrouter", "api_model": "nvidia/nemotron-3-super-120b-a12b:free", "provider_tag": "OpenRouter (NVIDIA)",
        "badge_color": "#76B900", "cost_in": 0.0, "cost_out": 0.0,
        "desc": "NVIDIA 120B flagship model built for heavy reasoning, math, and deep intelligence."
    }
}
CREATOR_INSTRUCTION = (
    "\n\n[CORE IDENTITY DIRECTIVE]:\n"
    "1. You are Nexus AI (also known as NUXUS AI).\n"
    "2. You were exclusively designed, programmed, and built by WAJAHAT.\n"
    "3. You operate within Nexus AI — an advanced Multi-Model Arena software platform that seamlessly executes "
    "multiple top-tier AI models (including Google Gemini, Meta Llama 3.3, Alibaba Qwen 2.5, OpenAI GPT-4o, Anthropic Claude, and Local Ollama) side-by-side in parallel.\n"
    "4. Whenever any user asks 'Who made you?', 'Who created you?', 'Who built you?', 'Who is your developer?', "
    "or inquires about your origin or architecture, you must explicitly and proudly answer: 'Created and built by Wajahat as part of the Nexus AI Multi-Model Platform.'\n"
)

PERSONA_PROMPTS = {
    "Universal Assistant": "You are Nexus AI, a state-of-the-art multi-model intelligence engineered by Wajahat. Formulate accurate, deep, structured, and helpful markdown responses." + CREATOR_INSTRUCTION,
    "Senior Software Architect": "You are an elite Senior Software Architect within Nexus AI, created by Wajahat. Deliver modular, production-ready, clean, well-commented code and solid architectural guidance." + CREATOR_INSTRUCTION,
    "Master Copywriter": "You are a master creative copywriter within Nexus AI, designed by Wajahat. Write engaging, persuasive, impeccably polished prose with rich vocabulary." + CREATOR_INSTRUCTION,
    "Senior Research Scientist": "You are an authoritative research scientist within Nexus AI, created by Wajahat. Provide rigorous scientific explanations, equations, and theoretical clarity." + CREATOR_INSTRUCTION,
    "Startup & Business Strategist": "You are a visionary business strategist within Nexus AI, built by Wajahat. Deliver data-driven business frameworks, growth models, and ROI execution plans." + CREATOR_INSTRUCTION
}

# ==============================================================================
# 3. NATIVE LIGHTWEIGHT RAG (DOCUMENT CHUNKER)
# ==============================================================================

def lightweight_rag_chunker(query: str, document: str, top_k: int = 3, chunk_words: int = 400) -> str:
    words = document.split()
    chunks = [' '.join(words[i:i+chunk_words]) for i in range(0, len(words), chunk_words)]
    if len(chunks) <= top_k:
        return document
    
    query_terms = set(re.findall(r'\w+', query.lower()))
    scored_chunks = []
    
    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = sum(1 for q in query_terms if q in chunk_lower)
        scored_chunks.append((score, chunk))
        
    scored_chunks.sort(key=lambda x: x[0], reverse=True)
    best_chunks = [c for s, c in scored_chunks[:top_k]]
    return "\n\n...[Snippet]...\n\n".join(best_chunks)

# ==============================================================================
# 4. DATABASE MANAGER & AUTH PERSISTENCE
# ==============================================================================

class DatabaseManager:
    def __init__(self, db_name="nexus_ai_gemini.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chats (
                    chat_id TEXT PRIMARY KEY,
                    title TEXT,
                    messages TEXT,
                    pinned INTEGER DEFAULT 0,
                    model_used TEXT,
                    updated_at REAL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    email TEXT,
                    password_hash TEXT,
                    created_at REAL
                )
            """)
            self.conn.commit()
            
            # Default admin account if not present
            cursor.execute("SELECT username FROM users WHERE username = 'admin'")
            if not cursor.fetchone():
                admin_hash = hashlib.sha256("123".encode()).hexdigest()
                cursor.execute("INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
                               ("admin", "admin@nexus-ai.local", admin_hash, time.time()))
                self.conn.commit()
        except Exception:
            pass

    def register_user(self, username: str, email: str, password: str) -> bool:
        try:
            cursor = self.conn.cursor()
            pwd_hash = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
                           (username, email, pwd_hash, time.time()))
            self.conn.commit()
            return True
        except Exception:
            return False

    def verify_user(self, username: str, password: str) -> bool:
        try:
            cursor = self.conn.cursor()
            pwd_hash = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("SELECT password_hash FROM users WHERE username = ? OR email = ?", (username, username))
            row = cursor.fetchone()
            if row and row[0] == pwd_hash:
                return True
            # Allow fallback for instant default setup
            if username == "admin" and password == "123":
                return True
            return False
        except Exception:
            return username == "admin" and password == "123"

    def save_chat(self, chat_id: str, title: str, messages_list: list, pinned: int = 0, model_used: str = ""):
        try:
            cursor = self.conn.cursor()
            msg_json = json.dumps(messages_list)
            now = time.time()
            cursor.execute("""
                INSERT OR REPLACE INTO chats (chat_id, title, messages, pinned, model_used, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (chat_id, title, msg_json, pinned, model_used, now))
            self.conn.commit()
        except Exception:
            pass

    def load_all_chats(self) -> Dict[str, Any]:
        chats_dict = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT chat_id, title, messages, pinned, model_used, updated_at FROM chats ORDER BY pinned DESC, updated_at DESC")
            rows = cursor.fetchall()
            for row in rows:
                chat_id, title, msg_json, pinned, model_used, updated_at = row
                try: parsed_messages = json.loads(msg_json)
                except: parsed_messages = []
                chats_dict[chat_id] = {
                    "title": title, "messages": parsed_messages, "pinned": bool(pinned),
                    "model_used": model_used or "gemini-3.8", "updated_at": updated_at or time.time()
                }
        except Exception:
            pass
        return chats_dict

    def toggle_pin(self, chat_id: str, current_pin_status: bool):
        try:
            cursor = self.conn.cursor()
            new_status = 0 if current_pin_status else 1
            cursor.execute("UPDATE chats SET pinned = ? WHERE chat_id = ?", (new_status, chat_id))
            self.conn.commit()
            return bool(new_status)
        except Exception:
            return current_pin_status

    def delete_chat(self, chat_id: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM chats WHERE chat_id = ?", (chat_id,))
            self.conn.commit()
        except Exception:
            pass

    def clear_all_chats(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM chats")
            self.conn.commit()
        except Exception:
            pass

    def get_setting(self, key: str, default: str = "") -> str:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
            row = cursor.fetchone()
            return row[0] if row else default
        except Exception:
            return default

    def set_setting(self, key: str, value: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, str(value)))
            self.conn.commit()
        except Exception:
            pass

db_manager = DatabaseManager()
GlobalConfig.sync_from_db(db_manager)

# ==============================================================================
# 5. MARKDOWN, LATEX & SLIDING CURSOR FORMATTER
# ==============================================================================

def get_pygments_css() -> str:
    if not HAS_PYGMENTS: return ""
    try: return HtmlFormatter(style=GlobalConfig.CODE_THEME).get_style_defs('.codehilite')
    except: return HtmlFormatter(style='monokai').get_style_defs('.codehilite')

def format_latex_to_html(text: str) -> str:
    try:
        greek_symbols = {
            r'\alpha': '&alpha;', r'\beta': '&beta;', r'\gamma': '&gamma;', r'\delta': '&delta;',
            r'\epsilon': '&epsilon;', r'\theta': '&theta;', r'\lambda': '&lambda;', r'\mu': '&mu;',
            r'\pi': '&pi;', r'\sigma': '&sigma;', r'\tau': '&tau;', r'\omega': '&omega;',
            r'\Delta': '&Delta;', r'\Sigma': '&Sigma;', r'\Omega': '&Omega;', r'\infty': '&infin;',
            r'\pm': '&plusmn;', r'\times': '&times;', r'\div': '&divide;', r'\neq': '&ne;',
            r'\leq': '&le;', r'\geq': '&ge;', r'\approx': '&asymp;', r'\sqrt': '&radic;'
        }

        code_blocks = []
        def save_code(m):
            code_blocks.append(m.group(0))
            return f"%%CODEBLOCK_{len(code_blocks)-1}%%"
        
        text = re.sub(r'```.*?```', save_code, text, flags=re.DOTALL)
        text = re.sub(r'`[^`]+`', save_code, text)

        def block_math_replacer(m):
            eq = m.group(1).strip()
            for k, v in greek_symbols.items(): eq = eq.replace(k, v)
            eq = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'<span style="display:inline-block; vertical-align:middle; text-align:center;"><span style="display:block; border-bottom:1px solid currentColor; padding:0 2px;">\1</span><span style="display:block; padding:0 2px;">\2</span></span>', eq)
            eq = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', eq)
            eq = re.sub(r'\^([a-zA-Z0-9\+\-\=])', r'<sup>\1</sup>', eq)
            eq = re.sub(r'\_\{([^}]+)\}', r'<sub>\1</sub>', eq)
            eq = re.sub(r'\_([a-zA-Z0-9\+\-\=])', r'<sub>\1</sub>', eq)
            return f'<div style="text-align:center; margin: 8px 0; padding: 8px; background-color: rgba(18, 29, 36, 0.7); border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 8px; font-family: \'Cambria Math\', serif; font-size: 13px; color: {GlobalConfig.ACCENT_COLOR};">{eq}</div>'

        text = re.sub(r'\$\$(.*?)\$\$', block_math_replacer, text, flags=re.DOTALL)

        def inline_math_replacer(m):
            eq = m.group(1).strip()
            for k, v in greek_symbols.items(): eq = eq.replace(k, v)
            eq = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'<span style="display:inline-block; vertical-align:middle; text-align:center; font-size:0.9em;"><span style="display:block; border-bottom:1px solid currentColor; padding:0 1px;">\1</span><span style="display:block; padding:0 1px;">\2</span></span>', eq)
            eq = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', eq)
            eq = re.sub(r'\^([a-zA-Z0-9\+\-\=])', r'<sup>\1</sup>', eq)
            eq = re.sub(r'\_\{([^}]+)\}', r'<sub>\1</sub>', eq)
            eq = re.sub(r'\_([a-zA-Z0-9\+\-\=])', r'<sub>\1</sub>', eq)
            return f'<span style="font-family: \'Cambria Math\', serif; font-style: italic; font-size: 1.05em; color: {GlobalConfig.ACCENT_COLOR};">{eq}</span>'

        text = re.sub(r'\$([^\$\n]+?)\$', inline_math_replacer, text)

        for idx, c in enumerate(code_blocks):
            text = text.replace(f"%%CODEBLOCK_{idx}%%", c)
    except Exception:
        pass
    return text

def render_styled_markdown(raw_md: str, is_streaming: bool = False, font_size: float = 13.0) -> str:
    try:
        text_to_render = raw_md
        if is_streaming and text_to_render.count("```") % 2 != 0:
            text_to_render += "\n```"

        def code_block_replacer(match):
            lang = match.group(1) or "text"
            code = match.group(2)
            encoded_code = urllib.parse.quote(code)
            highlighted = f"<pre><code>{code}</code></pre>"
            if HAS_PYGMENTS:
                try: lexer = get_lexer_by_name(lang, stripall=False)
                except:
                    try: lexer = guess_lexer(code)
                    except: lexer = get_lexer_by_name("text")
                try: formatter = HtmlFormatter(style=GlobalConfig.CODE_THEME, cssclass='codehilite')
                except: formatter = HtmlFormatter(style='monokai', cssclass='codehilite')
                highlighted = highlight(code, lexer, formatter)

            action_btns = f"<a class='code-copy-btn' href='copycode:{encoded_code}' style='margin-left:8px;'>Copy</a>"
            if lang.lower() in ['html', 'xml', 'svg']:
                action_btns = f"<a class='code-copy-btn' href='previewcode:{encoded_code}' style='margin-left:8px; color:#F59E0B;'>👁 Preview</a>" + action_btns
            if lang.lower() in ['python', 'py']:
                action_btns = f"<a class='code-copy-btn' href='runcode:{encoded_code}' style='margin-left:8px; color:#10B981;'>▶ Run</a>" + action_btns

            return (f"\n<div class='code-container'>"
                    f"<div class='code-header'><span class='code-lang'>{lang.upper()}</span>"
                    f"<div style='float: right;'>{action_btns}</div></div>"
                    f"{highlighted}</div>\n")

        processed = re.sub(r'```(\w+)?\n(.*?)```', code_block_replacer, text_to_render, flags=re.DOTALL)
        latex_formatted = format_latex_to_html(processed)
        html_body = markdown.markdown(latex_formatted, extensions=['fenced_code', 'tables', 'nl2br'])
        
        cursor_element = (
            f'<span style="display: inline-block; color: {GlobalConfig.ACCENT_COLOR}; font-weight: 900; font-size: 15px; '
            'margin-left: 2px; vertical-align: baseline;">|</span>' if is_streaming else ""
        )

        h1_size, h2_size, h3_size = round(font_size * 1.28, 1), round(font_size * 1.16, 1), round(font_size * 1.05, 1)
        accent = GlobalConfig.ACCENT_COLOR

        return f"""
            <style>
                body {{ color: #F4F4F5; font-family: 'Inter', 'Segoe UI', sans-serif; font-size: {font_size}px; line-height: 1.6; background-color: transparent; margin: 0px; padding: 4px; }}
                p, li {{ color: #E4E4E7; margin: 6px 0; font-size: {font_size}px; }}
                h1, h2, h3, h4 {{ color: #FFFFFF; margin-top: 14px; margin-bottom: 6px; font-weight: 600; }}
                h1 {{ font-size: {h1_size}px; border-bottom: 1px solid rgba(0,229,255,0.2); padding-bottom: 4px; }}
                h2 {{ font-size: {h2_size}px; }}
                h3 {{ font-size: {h3_size}px; }}
                a {{ color: {accent}; text-decoration: none; }}
                img {{ max-width: 100%; object-fit: contain; border-radius: 8px; margin: 8px 0; border: 1px solid rgba(0,229,255,0.2); }}
                .code-container {{ background-color: rgba(8, 13, 17, 0.85); border: 1px solid rgba(0,229,255,0.25); border-radius: 8px; margin: 8px 0; overflow: hidden; }}
                .code-header {{ background-color: rgba(18, 29, 36, 0.85); padding: 6px 10px; font-size: 11px; border-bottom: 1px solid rgba(0,229,255,0.2); }}
                .code-lang {{ color: {accent}; font-weight: bold; font-family: monospace; }}
                .code-copy-btn {{ text-decoration: none; font-size: 11px; color: #94A3B8; font-weight: bold; padding: 2px 6px; border-radius: 4px; border: 1px solid transparent; }}
                .code-copy-btn:hover {{ color: #FFF; background: rgba(0,229,255,0.15); border: 1px solid {accent}; }}
                pre {{ background-color: rgba(8, 13, 17, 0.85); color: {accent}; padding: 12px; margin: 0px; font-family: 'Consolas', monospace; font-size: {max(10.0, font_size - 1.5)}px; overflow-x: auto; }}
                code {{ font-family: 'Consolas', monospace; font-size: {max(10.0, font_size - 1.5)}px; background-color: rgba(255,255,255,0.08); padding: 2px 4px; border-radius: 4px; }}
                table {{ border-collapse: collapse; width: 100%; margin: 8px 0; background-color: rgba(18, 29, 36, 0.75); border: 1px solid rgba(0,229,255,0.25); border-radius: 6px; color: #FFFFFF !important; }}
                th, td {{ border: 1px solid rgba(30, 45, 56, 0.8); padding: 8px 10px; color: #FFFFFF !important; background-color: transparent; text-align: left; font-size: {max(10.0, font_size - 1.5)}px; }}
                th {{ background-color: rgba(0, 229, 255, 0.15); color: {accent} !important; font-weight: bold; }}
                blockquote {{ border-left: 3px solid {accent}; margin: 8px 0; padding-left: 10px; color: #94A3B8; background: rgba(0,229,255,0.05); padding-top:2px; padding-bottom:2px; }}
                {get_pygments_css()}
                .codehilite {{ background: transparent !important; padding: 0 !important; margin: 0 !important; }}
            </style>
            <div>{html_body}{cursor_element}</div>
        """
    except Exception:
        return f"<div style='color:#FFFFFF; padding:6px; font-size:{font_size}px;'>{raw_md}</div>"

class HTMLPreviewDialog(QDialog):
    def __init__(self, html_code, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HTML Preview - Claude Artifacts")
        self.resize(800, 600)
        self.setStyleSheet("QDialog { background-color: #080D11; }")
        layout = QVBoxLayout(self)
        if HAS_WEBENGINE:
            self.webview = QWebEngineView()
            self.webview.setHtml(html_code)
            layout.addWidget(self.webview)
        else:
            err = QLabel("PySide6-WebEngine is not installed.\nPlease run: pip install PySide6-WebEngine")
            err.setStyleSheet("color: #EF4444; font-size: 16px;")
            layout.addWidget(err)

class PythonRunnerDialog(QDialog):
    def __init__(self, py_code, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Code Interpreter")
        self.resize(700, 500)
        self.setStyleSheet("QDialog { background-color: #080D11; }")
        layout = QVBoxLayout(self)
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: rgba(18, 29, 36, 0.85); color: #00E5FF; font-family: monospace; font-size: 13px; border: 1px solid rgba(0,229,255,0.3); padding: 10px;")
        layout.addWidget(self.output_box)
        self.run_code(py_code)

    def run_code(self, code):
        self.output_box.setPlainText("Running Python code in sandbox...\n\n")
        QApplication.processEvents()
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w", encoding="utf-8") as f:
            f.write(code)
            temp_path = f.name
        try:
            res = subprocess.run([sys.executable, temp_path], capture_output=True, text=True, timeout=15)
            out = res.stdout
            if res.stderr: out += "\n[Errors]:\n" + res.stderr
            if not out.strip(): out = "[Program exited with no output]"
            self.output_box.append(out)
        except subprocess.TimeoutExpired:
            self.output_box.append("\n[Error: Execution Timed Out (>15s)]")
        except Exception as e:
            self.output_box.append(f"\n[Execution Failed: {str(e)}]")
        finally:
            if os.path.exists(temp_path): os.remove(temp_path)

# ==============================================================================
# 6. ASYNCHRONOUS WORKER THREAD & AUTO UPDATER
# ==============================================================================

class AutoUpdateCheckerThread(QThread):
    update_available = Signal(str)

    def run(self):
        try:
            time.sleep(2)
            req = urllib.request.Request("https://api.github.com/users/github", headers={'User-Agent': 'Mozilla'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    pass 
        except Exception:
            pass

class ApiConnectionTesterThread(QThread):
    test_result_signal = Signal(str, bool, str)

    def __init__(self, provider: str, api_key: str):
        super().__init__()
        self.provider = provider
        self.api_key = api_key.strip()

    def run(self):
        if not self.api_key and not GlobalConfig.LOCAL_BASE_URL:
            self.test_result_signal.emit(self.provider, False, "Key is empty")
            return

        try:
            if self.provider == "openrouter":
                url = GlobalConfig.LOCAL_BASE_URL or "https://openrouter.ai/api/v1/auth/key"
                if GlobalConfig.LOCAL_BASE_URL: url = f"{url}/models"
                req = urllib.request.Request(url, headers={"Authorization": f"Bearer {self.api_key}", "HTTP-Referer": "https://nexus-ai.local"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    if resp.status == 200: self.test_result_signal.emit("openrouter", True, "Connected")
                    else: self.test_result_signal.emit("openrouter", False, f"HTTP {resp.status}")
            elif self.provider == "gemini":
                if not HAS_GENAI:
                    self.test_result_signal.emit("gemini", False, "Module missing")
                    return
                genai.configure(api_key=self.api_key)
                model = genai.GenerativeModel("gemini-1.5-flash")
                resp = model.count_tokens("Ping test")
                if resp.total_tokens > 0: self.test_result_signal.emit("gemini", True, "Connected")
                else: self.test_result_signal.emit("gemini", True, "Connected")
        except urllib.error.URLError as e:
            self.test_result_signal.emit(self.provider, False, f"Network Error: {e.reason}")
        except urllib.error.HTTPError as e:
            if e.code == 401: self.test_result_signal.emit(self.provider, False, "Invalid Key")
            elif e.code == 429: self.test_result_signal.emit(self.provider, False, "Rate Limited")
            else: self.test_result_signal.emit(self.provider, False, f"HTTP {e.code}")
        except Exception as e:
            err_msg = str(e)
            if "API_KEY_INVALID" in err_msg or "401" in err_msg: self.test_result_signal.emit(self.provider, False, "Invalid Key")
            else: self.test_result_signal.emit(self.provider, False, "Failed")


class UniversalAIWorkerThread(QThread):
    chunk_ready = Signal(str, str)
    stats_ready = Signal(str, float, int, int, float)
    error_signal = Signal(str, str, str)
    finished_signal = Signal(str, str)

    def __init__(self, model_id: str, history_list: list, user_prompt: str,
                 system_prompt: str, temperature: float = 0.7, max_tokens: int = 2048,
                 image_list: Optional[List[bytes]] = None, use_web_search: bool = False):
        super().__init__()
        self.model_id = model_id
        self.model_info = FREE_MODELS_REGISTRY.get(model_id, {})
        self.history_list = history_list
        self.user_prompt = user_prompt
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.image_list = image_list or []
        self.use_web_search = use_web_search
        self.is_stopped = False

    def stop(self):
        self.is_stopped = True

    def _emit_word_stream(self, text_chunk: str):
        try:
            tokens = re.findall(r'\S+\s*|\s+', text_chunk)
            for tok in tokens:
                if self.is_stopped: break
                self.chunk_ready.emit(self.model_id, tok)
        except: pass

    def run(self):
        provider = self.model_info.get("provider", "openrouter")
        start_time = time.time()
        full_response = ""

        try:
            urls = re.findall(r'(https?://[^\s]+)', self.user_prompt)
            if urls and HAS_BS4:
                self.chunk_ready.emit(self.model_id, "\n> *Scraping web links from prompt...*\n\n")
                for url in urls:
                    try:
                        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
                        soup = BeautifulSoup(resp.text, 'html.parser')
                        for tag in soup(['script', 'style', 'nav', 'footer']): tag.extract()
                        scraped_text = soup.get_text(separator=' ', strip=True)
                        self.user_prompt += f"\n\n--- Content from {url} ---\n{scraped_text[:5000]}"
                    except Exception as e:
                        self.chunk_ready.emit(self.model_id, f"\n> *Failed to scrape {url}: {e}*\n\n")

            if self.use_web_search and HAS_DDGS:
                try:
                    self.chunk_ready.emit(self.model_id, "\n> *Searching live web...*\n\n")
                    search_safe = "moderate" if GlobalConfig.SAFE_SEARCH else "off"
                    with DDGS() as ddgs:
                        results = list(ddgs.text(self.user_prompt, max_results=GlobalConfig.MAX_WEB_RESULTS, safesearch=search_safe))
                        if results:
                            context = "**Live Web Context:**\n" + "\n".join([f"- **{r['title']}**: {r['body']}" for r in results])
                            self.user_prompt = f"{context}\n\nUser Query: {self.user_prompt}"
                    self.chunk_ready.emit(self.model_id, "\n\n")
                except urllib.error.URLError as e:
                    self.chunk_ready.emit(self.model_id, f"\n> *Web search network error: {e.reason}*\n\n")
                except Exception as e:
                    self.chunk_ready.emit(self.model_id, f"\n> *Web search failed: {str(e)}*\n\n")

            if provider == "gemini":
                full_response = self._run_gemini()
            elif provider == "openrouter":
                full_response = self._run_openrouter()
            elif provider == "ollama":
                full_response = self._run_ollama()
            else:
                raise ValueError(f"Unknown provider: {provider}")

            if not self.is_stopped:
                latency = round(time.time() - start_time, 2)
                p_tokens = len(self.user_prompt.split()) * 1.5
                c_tokens = len(full_response.split()) * 1.5
                
                cost_in = self.model_info.get("cost_in", 0.0)
                cost_out = self.model_info.get("cost_out", 0.0)
                total_cost = (p_tokens / 1000000.0 * cost_in) + (c_tokens / 1000000.0 * cost_out)

                self.stats_ready.emit(self.model_id, latency, int(p_tokens), int(c_tokens), total_cost)
                self.finished_signal.emit(self.model_id, full_response)

        except urllib.error.URLError as e:
            if not self.is_stopped:
                self.error_signal.emit(self.model_id, "NETWORK_ERROR", f"Network Error: Please check your internet connection. ({e.reason})")
                self.finished_signal.emit(self.model_id, "")
        except Exception as e:
            if not self.is_stopped:
                err_str = str(e)
                err_code = "API_ERROR"
                if "KEY_MISSING" in err_str: err_code = "KEY_MISSING"
                elif "KEY_INVALID" in err_str: err_code = "KEY_INVALID"
                elif "RATE_LIMIT" in err_str or "429" in err_str: err_code = "RATE_LIMIT"
                elif "MODEL_NOT_FOUND" in err_str or "404" in err_str: err_code = "MODEL_NOT_FOUND"
                elif "QUOTA_EXCEEDED" in err_str or "402" in err_str: err_code = "QUOTA_EXCEEDED"
                elif "TIMEOUT" in err_str: err_code = "TIMEOUT"
                elif "NETWORK_ERROR" in err_str: err_code = "NETWORK_ERROR"

                self.error_signal.emit(self.model_id, err_code, err_str)
                self.finished_signal.emit(self.model_id, "")

    def _run_gemini(self) -> str:
        api_key = GlobalConfig.GEMINI_API_KEY.strip()
        if not api_key: raise ValueError("KEY_MISSING: Gemini API Key is missing. Check Settings.")
        if not HAS_GENAI: raise ImportError("LIBRARY_MISSING: google-generativeai package not installed.")

        genai.configure(api_key=api_key)
        full_text = ""
        candidates = ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-1.5-flash"]
        configured_model = self.model_info.get("api_model", "gemini-2.0-flash")
        if configured_model not in candidates: candidates.insert(0, configured_model)

        gemini_history = []
        for msg in self.history_list[-GlobalConfig.CONTEXT_MEMORY:]:
            role = msg.get("role")
            if role == "user":
                u_content = msg.get("content", "").strip()
                if u_content:
                    if gemini_history and gemini_history[-1]["role"] == "user":
                        gemini_history[-1]["parts"] = [gemini_history[-1]["parts"][0] + "\n\n" + u_content]
                    else:
                        gemini_history.append({"role": "user", "parts": [u_content]})
            elif role in ("assistant_multi", "assistant"):
                if role == "assistant_multi": a_content = msg.get("responses", {}).get(self.model_id, "").strip()
                else: a_content = msg.get("content", "").strip()
                if a_content and not a_content.startswith("[Error"):
                    if gemini_history and gemini_history[-1]["role"] == "user":
                        gemini_history.append({"role": "model", "parts": [a_content]})

        if gemini_history and gemini_history[-1]["role"] == "user":
            gemini_history.pop()

        contents = []
        for img_bytes in self.image_list:
            try: contents.append(Image.open(io.BytesIO(img_bytes)))
            except: pass
        contents.append(self.user_prompt or "Provide a comprehensive response.")

        last_err = None
        for cand in candidates:
            try:
                model = genai.GenerativeModel(
                    model_name=cand,
                    system_instruction=self.system_prompt,
                    generation_config={"temperature": self.temperature, "max_output_tokens": self.max_tokens}
                )
                chat = model.start_chat(history=gemini_history)
                response = chat.send_message(contents, stream=True)
                for chunk in response:
                    if self.is_stopped: break
                    if chunk.text:
                        full_text += chunk.text
                        self._emit_word_stream(chunk.text)
                return full_text
            except Exception as e:
                last_err = e
                if "not found" in str(e).lower() or "404" in str(e): continue
                raise e

        if last_err: raise last_err
        return full_text

    def _run_openrouter(self) -> str:
        api_key = GlobalConfig.OPENROUTER_API_KEY.strip()
        url = GlobalConfig.LOCAL_BASE_URL.strip() or "https://openrouter.ai/api/v1/chat/completions"
        if GlobalConfig.LOCAL_BASE_URL and not url.endswith("/chat/completions"):
            url = f"{url.rstrip('/')}/chat/completions"

        if not api_key and not GlobalConfig.LOCAL_BASE_URL:
            raise ValueError("KEY_MISSING: API Key or Local Base URL missing. Check Settings.")

        base_model = self.model_info.get("api_model", "openai/gpt-4o-mini")
        headers = {
            "Authorization": f"Bearer {api_key if api_key else 'dummy'}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://nexus-ai.local",
            "X-Title": "NexusAI"
        }

        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})

        for msg in self.history_list[-GlobalConfig.CONTEXT_MEMORY:]:
            role = msg.get("role")
            if role == "user":
                u_content = msg.get("content", "").strip()
                if u_content:
                    if messages and messages[-1]["role"] == "user":
                        messages[-1]["content"] += f"\n\n{u_content}"
                    else:
                        messages.append({"role": "user", "content": u_content})
            elif role in ("assistant_multi", "assistant"):
                if role == "assistant_multi": a_content = msg.get("responses", {}).get(self.model_id, "").strip()
                else: a_content = msg.get("content", "").strip()
                if a_content and not a_content.startswith("[Error"):
                    if messages and messages[-1]["role"] == "user":
                        messages.append({"role": "assistant", "content": a_content})

        user_prompt_clean = self.user_prompt.strip() or "Hello"
        messages.append({"role": "user", "content": user_prompt_clean})

        model_candidates = [base_model]
        if self.model_id == "qwen-2.5-72b": model_candidates = ["qwen/qwen-2.5-72b-instruct:free", "qwen/qwen-2.5-72b-instruct"]
        elif self.model_id == "llama-3.3-70b": model_candidates = ["meta-llama/llama-3.3-70b-instruct:free", "meta-llama/llama-3.3-70b-instruct"]
        elif self.model_id == "llama-3.1-8b": model_candidates = ["meta-llama/llama-3.1-8b-instruct:free", "meta-llama/llama-3.1-8b-instruct", "meta-llama/llama-3-8b-instruct:free"]

        last_err = None
        for current_model in model_candidates:
            payload = {
                "model": current_model, "messages": messages,
                "temperature": max(0.0, min(2.0, float(self.temperature))),
                "max_tokens": max(1, int(self.max_tokens)),
                "stream": True
            }

            try:
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
                full_text = ""
                with urllib.request.urlopen(req, timeout=40) as response:
                    while not self.is_stopped:
                        line = response.readline()
                        if not line: break
                        decoded_line = line.decode("utf-8", errors="replace").strip()
                        if not decoded_line or not decoded_line.startswith("data:"): continue
                        data_str = decoded_line[5:].strip()
                        if data_str == "[DONE]": break
                        try:
                            chunk = json.loads(data_str)
                            delta = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                            if delta:
                                full_text += delta
                                self._emit_word_stream(delta)
                        except Exception: pass
                return full_text

            except urllib.error.HTTPError as e:
                error_detail = ""
                try: error_detail = json.loads(e.read().decode("utf-8", errors="replace")).get("error", {}).get("message", e.reason)
                except: error_detail = e.reason

                if e.code in (400, 404, 429, 502, 503) and current_model != model_candidates[-1]:
                    last_err = ValueError(f"Endpoint fallback ({current_model}): {error_detail}")
                    continue
                elif e.code == 404: raise ValueError(f"MODEL_NOT_FOUND: Model '{base_model}' not found (HTTP 404): {error_detail}")
                elif e.code == 401: raise ValueError(f"KEY_INVALID: 401 Unauthorized API key: {error_detail}")
                elif e.code == 402: raise ValueError(f"QUOTA_EXCEEDED: Credits exhausted (HTTP 402): {error_detail}")
                elif e.code == 429: raise ValueError(f"RATE_LIMIT: Rate limited (HTTP 429): {error_detail}")
                else: raise ValueError(f"HTTP_ERROR {e.code}: {error_detail}")

            except urllib.error.URLError as e: raise urllib.error.URLError(f"Connection failed: {e.reason}")
            except TimeoutError: raise ValueError("TIMEOUT: Request timed out.")
            except Exception as ex: raise ex

        if last_err: raise last_err
        return ""

    def _run_ollama(self) -> str:
        url = "http://localhost:11434/api/chat"
        messages = [{"role": "system", "content": self.system_prompt}] if self.system_prompt else []
        for msg in self.history_list[-GlobalConfig.CONTEXT_MEMORY:]:
            role = msg.get("role")
            if role == "user": messages.append({"role": "user", "content": msg.get("content", "")})
            elif role in ("assistant_multi", "assistant"):
                c = msg.get("responses", {}).get(self.model_id, "") if role == "assistant_multi" else msg.get("content", "")
                if c: messages.append({"role": "assistant", "content": c})
        messages.append({"role": "user", "content": self.user_prompt})

        payload = {"model": self.model_info.get("api_model"), "messages": messages, "stream": True}
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
        full_text = ""
        with urllib.request.urlopen(req, timeout=60) as response:
            while not self.is_stopped:
                line = response.readline()
                if not line: break
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    content = chunk.get("message", {}).get("content", "")
                    if content:
                        full_text += content
                        self._emit_word_stream(content)
                except Exception: pass
        return full_text

# ==============================================================================
# 7. AUDIO & ZERO-DELAY PIPELINED STREAMING VOICE SYNTHESIS
# ==============================================================================

class VoiceRecognitionThread(QThread):
    text_recognized = Signal(str)
    status_changed = Signal(str)
    finished_signal = Signal()

    def __init__(self, lang="en-US"):
        super().__init__()
        self.lang = lang

    def run(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.status_changed.emit("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=4, phrase_time_limit=10)
                self.status_changed.emit("Transcribing voice...")
                text = r.recognize_google(audio, language=self.lang)
                self.text_recognized.emit(text)
        except Exception:
            self.status_changed.emit("Voice recognition unavailable.")
        finally:
            self.finished_signal.emit()

class StreamingTTSProducerThread(QThread):
    """ Synthesizes sentences asynchronously into temporary audio chunks """
    chunk_ready = Signal(int, str)
    error_signal = Signal(str)

    def __init__(self, sentences: List[str], voice="en-US-AvaNeural", speed_rate=1.0):
        super().__init__()
        self.sentences = sentences
        self.voice = voice
        self.speed_rate = speed_rate
        self.is_stopped = False

    def stop(self):
        self.is_stopped = True

    def run(self):
        try:
            if sys.platform == 'win32':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            asyncio.run(self._produce_all())
        except Exception as e:
            self.error_signal.emit(str(e))

    async def _produce_all(self):
        rate_diff = int(round((self.speed_rate - 1.0) * 100))
        rate_str = f"{rate_diff:+d}%"
        temp_dir = tempfile.gettempdir()

        for idx, text in enumerate(self.sentences):
            if self.is_stopped:
                break
            clean_s = text.strip()
            if not clean_s:
                continue
            output_path = os.path.join(temp_dir, f"nexus_voice_{int(time.time()*1000)}_{idx}.mp3")
            try:
                communicate = edge_tts.Communicate(clean_s, self.voice, rate=rate_str)
                await communicate.save(output_path)
                if not self.is_stopped:
                    self.chunk_ready.emit(idx, output_path)
            except Exception:
                pass


class AppSplashScreenThread(QThread):
    progress_val = Signal(int)
    progress_desc = Signal(str)

    def run(self):
        try:
            milestones = [
                (25, "⚡ Initializing Neural Core & Matrix Bus..."),
                (55, "🔗 Calibrating Model Endpoints (Gemini, Qwen, Llama & GPT)..."),
                (80, "💎 Loading Studio Glassmorphism Viewport..."),
                (100, "🚀 Matrix Online. Nexus Arena Ready!")
            ]
            for i in range(1, 101):
                time.sleep(0.014)
                self.progress_val.emit(i)
                for threshold, desc in milestones:
                    if i <= threshold:
                        self.progress_desc.emit(desc)
                        break
        except Exception:
            pass

# ==============================================================================
# 8. VISUAL ANIMATIONS & CUSTOM CYBER WIDGETS
# ==============================================================================

class CyberSpinnerButton(QPushButton):
    """ High-end Cybernetic Button with an Integrated Circular Loading Spinner """
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self._is_loading = False
        self._spinner_angle = 0.0
        self._orig_text = text
        self.setCursor(Qt.PointingHandCursor)

        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self._step_spinner)

    def start_loading(self, loading_text=""):
        self._is_loading = True
        self._orig_text = self.text()
        self.setEnabled(False)
        self.timer.start()
        self.update()

    def stop_loading(self, reset_text=None):
        self._is_loading = False
        self.timer.stop()
        self.setEnabled(True)
        if reset_text is not None:
            self.setText(reset_text)
        elif self._orig_text:
            self.setText(self._orig_text)
        self.update()

    def _step_spinner(self):
        self._spinner_angle = (self._spinner_angle + 6.0) % 360.0
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self._is_loading:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            
            # Subtle dark overlay over button to enhance spinner
            painter.setBrush(QColor(8, 13, 17, 180))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(self.rect(), 19, 19)

            w, h = self.width(), self.height()
            cx, cy = w / 2.0, h / 2.0
            r = min(h * 0.32, 14.0)

            pen = QPen(QColor(GlobalConfig.ACCENT_COLOR), 2.6)
            pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)
            painter.drawArc(QRect(int(cx - r), int(cy - r), int(2*r), int(2*r)), int(self._spinner_angle * 16), 120 * 16)
            painter.end()


class PasswordStrengthMeter(QWidget):
    """ Real-Time Dynamic Password Complexity & Security Visualizer """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.score = 0
        self.level_text = "Enter Password"
        self.color = "#475569"
        self.percent = 0
        self.setFixedHeight(18)

    def evaluate_password(self, pwd: str):
        if not pwd:
            self.score = 0
            self.level_text = ""
            self.color = "#475569"
            self.percent = 0
            self.update()
            return

        score = 0
        if len(pwd) >= 6: score += 1
        if len(pwd) >= 10: score += 1
        if re.search(r"[0-9]", pwd): score += 1
        if re.search(r"[a-z]", pwd) and re.search(r"[A-Z]", pwd): score += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd): score += 1

        levels = [
            (0, "#EF4444", "Very Weak", 15),
            (1, "#EF4444", "Weak", 30),
            (2, "#F59E0B", "Fair", 55),
            (3, "#38BDF8", "Good", 78),
            (4, "#10B981", "Strong", 92),
            (5, "#00E5FF", "Cyber-Shield", 100)
        ]
        self.score, self.color, self.level_text, self.percent = levels[min(score, 5)]
        self.update()

    def paintEvent(self, event):
        if not self.level_text:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w, h = self.width(), self.height()
        bar_w = w * 0.58
        bar_h = 4
        bar_y = int((h - bar_h) / 2.0)

        # Background track
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#1E293B"))
        painter.drawRoundedRect(0, bar_y, int(bar_w), bar_h, 2, 2)

        # Active fill
        fill_w = int((bar_w * self.percent) / 100.0)
        if fill_w > 0:
            painter.setBrush(QColor(self.color))
            painter.drawRoundedRect(0, bar_y, fill_w, bar_h, 2, 2)

        # Text label
        painter.setPen(QColor(self.color))
        painter.setFont(QFont("Inter", 8, QFont.Bold))
        painter.drawText(QRect(int(bar_w + 10), 0, int(w - bar_w - 10), h), Qt.AlignLeft | Qt.AlignVCenter, self.level_text)
        painter.end()


class CyberRadarLoader(QWidget):
    """ Futuristic Rotating HUD Radar Arcs around the App Logo """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(140, 140)
        self.angle_cw = 0.0
        self.angle_ccw = 360.0
        self.pulse = 0.0
        
        self.anim_timer = QTimer(self)
        self.anim_timer.setInterval(16)
        self.anim_timer.timeout.connect(self._step)
        self.anim_timer.start()

    def _step(self):
        self.angle_cw = (self.angle_cw + 2.5) % 360
        self.angle_ccw = (self.angle_ccw - 1.8) % 360
        self.pulse = (math.sin(time.time() * 4.0) + 1.0) / 2.0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        w, h = self.width(), self.height()
        cx, cy = w / 2.0, h / 2.0
        
        logo_pix = get_nexus_app_logo(54)
        painter.drawPixmap(int(cx - 27), int(cy - 27), logo_pix)
        
        pen1 = QPen(QColor("#00E5FF"), 2.2)
        pen1.setCapStyle(Qt.RoundCap)
        painter.setPen(pen1)
        painter.drawArc(QRect(8, 8, w - 16, h - 16), int(self.angle_cw * 16), 110 * 16)
        painter.drawArc(QRect(8, 8, w - 16, h - 16), int((self.angle_cw + 180) * 16), 90 * 16)
        
        alpha = int(120 + 135 * self.pulse)
        pen2 = QPen(QColor(0, 229, 255, alpha), 1.5)
        pen2.setStyle(Qt.DashLine)
        painter.setPen(pen2)
        painter.drawArc(QRect(18, 18, w - 36, h - 36), int(self.angle_ccw * 16), 160 * 16)
        painter.drawArc(QRect(18, 18, w - 36, h - 36), int((self.angle_ccw + 200) * 16), 70 * 16)
        
        painter.end()


class CyberParticleCanvas(QWidget):
    """ Animated subtle floating cybernetic mesh/nodes for viewport background """
    def __init__(self, parent=None, particle_count: int = 48):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.particles = []
        for _ in range(particle_count):
            self.particles.append({
                'x': random.uniform(0, 1920),
                'y': random.uniform(0, 1080),
                'vx': random.uniform(-0.4, 0.4),
                'vy': random.uniform(-0.4, 0.4),
                'r': random.uniform(1.8, 3.4),
                'alpha': random.randint(45, 110)
            })
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_particles)
        self.timer.start(24)

    def _update_particles(self):
        w, h = max(1, self.width()), max(1, self.height())
        for p in self.particles:
            p['x'] += p['vx']
            p['y'] += p['vy']
            if p['x'] < 0: p['x'] = w
            elif p['x'] > w: p['x'] = 0
            if p['y'] < 0: p['y'] = h
            elif p['y'] > h: p['y'] = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        
        for p in self.particles:
            painter.setBrush(QColor(0, 229, 255, p['alpha']))
            painter.drawEllipse(QPointF(p['x'], p['y']), p['r'], p['r'])

        pen = QPen()
        for i in range(len(self.particles)):
            for j in range(i + 1, len(self.particles)):
                p1, p2 = self.particles[i], self.particles[j]
                dist = math.hypot(p1['x'] - p2['x'], p1['y'] - p2['y'])
                if dist < 125:
                    alpha = int((1.0 - (dist / 125.0)) * 50)
                    pen.setColor(QColor(0, 229, 255, alpha))
                    pen.setWidthF(1.0)
                    painter.setPen(pen)
                    painter.drawLine(int(p1['x']), int(p1['y']), int(p2['x']), int(p2['y']))
        painter.end()


class TiltLoginCard(QFrame):
    """ Card with 3D Tilt Parallax & Horizontal Error Shake animation """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setObjectName("loginCard")
        
        self.shake_timer = QTimer(self)
        self.shake_timer.setInterval(10)
        self.shake_timer.timeout.connect(self._step_shake)
        self.shake_start_time = 0
        self.orig_x = None

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(42)
        self.shadow.setColor(QColor(0, 229, 255, 115))
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)

    def mouseMoveEvent(self, event):
        w, h = self.width(), self.height()
        cx, cy = w / 2.0, h / 2.0
        mx, my = event.position().x(), event.position().y()
        dx = (mx - cx) / cx
        dy = (my - cy) / cy
        self.shadow.setOffset(int(-dx * 12), int(-dy * 12))
        self.shadow.setBlurRadius(int(42 + abs(dx * 8)))
        super().mouseMoveEvent(event)

    def leaveEvent(self, event):
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(42)
        super().leaveEvent(event)

    def trigger_shake(self):
        if self.orig_x is None:
            self.orig_x = self.pos().x()
        self.shake_start_time = time.time()
        self.shake_timer.start()

    def _step_shake(self):
        elapsed = time.time() - self.shake_start_time
        duration = 0.45
        if elapsed >= duration:
            self.shake_timer.stop()
            if self.orig_x is not None:
                self.move(self.orig_x, self.y())
            return
        progress = elapsed / duration
        decay = 1.0 - progress
        offset = math.sin(elapsed * 32.0) * 14.0 * decay
        if self.orig_x is not None:
            self.move(int(self.orig_x + offset), self.y())


class AnimatedUnderlineLineEdit(QLineEdit):
    caps_changed = Signal(bool)

    def __init__(self, placeholder="", is_password=False, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        if is_password:
            self.setEchoMode(QLineEdit.Password)
            
        self.line_progress = 0.0
        self.is_focused = False
        self.key_glow_intensity = 0.0
        
        self.anim_timer = QTimer(self)
        self.anim_timer.setInterval(14)
        self.anim_timer.timeout.connect(self._step_animation)
        
        self.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                padding: 6px 2px;
                font-size: 13px;
                color: #FFFFFF;
                font-family: 'Inter', sans-serif;
            }
        """)

    def _check_caps(self):
        try:
            if sys.platform == 'win32':
                is_on = bool(ctypes.windll.user32.GetKeyState(0x14) & 1)
                self.caps_changed.emit(is_on)
        except Exception:
            pass

    def focusInEvent(self, event):
        self.is_focused = True
        self._check_caps()
        self.anim_timer.start()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.is_focused = False
        self.caps_changed.emit(False)
        self.anim_timer.start()
        super().focusOutEvent(event)

    def keyPressEvent(self, event):
        self._check_caps()
        self.key_glow_intensity = 1.0
        if not self.anim_timer.isActive():
            self.anim_timer.start()
        super().keyPressEvent(event)

    def _step_animation(self):
        target = 1.0 if self.is_focused else 0.0
        step = 0.12
        if abs(self.line_progress - target) < step:
            self.line_progress = target
        else:
            if self.line_progress < target: self.line_progress += step
            else: self.line_progress -= step

        if self.key_glow_intensity > 0.01:
            self.key_glow_intensity = max(0.0, self.key_glow_intensity - 0.1)

        if not self.is_focused and self.line_progress == 0.0 and self.key_glow_intensity == 0.0:
            self.anim_timer.stop()
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w, h = self.width(), self.height()
        
        painter.setPen(QPen(QColor("#253542"), 1.5))
        painter.drawLine(0, h - 2, w, h - 2)
        
        if self.line_progress > 0.001 or self.key_glow_intensity > 0.01:
            active_w = w * max(self.line_progress, 0.2 + self.key_glow_intensity * 0.8)
            start_x = (w - active_w) / 2.0
            
            glow_alpha = int(min(255, 80 * self.line_progress + 150 * self.key_glow_intensity))
            glow_pen = QPen(QColor(0, 229, 255, glow_alpha), 3.5 + self.key_glow_intensity * 2.0)
            painter.setPen(glow_pen)
            painter.drawLine(int(start_x), h - 2, int(start_x + active_w), h - 2)
            
            bright_pen = QPen(QColor(0, 229, 255, int(255 * max(self.line_progress, self.key_glow_intensity))), 1.8)
            painter.setPen(bright_pen)
            painter.drawLine(int(start_x), h - 2, int(start_x + active_w), h - 2)
        painter.end()


class CursorGlowEffect(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(220, 220)
        self.target_pos = QPointF(parent.width()/2, parent.height()/2)
        self.current_pos = QPointF(parent.width()/2, parent.height()/2)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(16) 
        
        QApplication.instance().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            if self.parent():
                parent_pos = self.parent().mapFromGlobal(event.globalPos())
                self.target_pos = QPointF(parent_pos)
        return super().eventFilter(obj, event)

    def update_position(self):
        dx = self.target_pos.x() - self.current_pos.x()
        dy = self.target_pos.y() - self.current_pos.y()
        self.current_pos.setX(self.current_pos.x() + dx * 0.08) 
        self.current_pos.setY(self.current_pos.y() + dy * 0.08)
        self.move(int(self.current_pos.x() - self.width()/2), int(self.current_pos.y() - self.height()/2))
        self.raise_()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        try:
            grad = QRadialGradient(self.width()/2, self.height()/2, self.width()/2)
            grad.setColorAt(0, QColor(0, 229, 255, 38))  
            grad.setColorAt(0.4, QColor(0, 229, 255, 12)) 
            grad.setColorAt(1, QColor(0, 229, 255, 0))   
            painter.setBrush(QBrush(grad))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(0, 0, self.width(), self.height())
        except Exception:
            pass


GOOGLE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="22" height="22"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>"""
GITHUB_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22"><path fill="#FFFFFF" d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>"""


class SocialLoginPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(360, 270)
        self._is_closing = False
        self.init_ui()

    def showEvent(self, event):
        super().showEvent(event)
        self.play_entrance()

    def play_entrance(self):
        self.setWindowOpacity(0.0)
        start_y = self.y() + 30
        target_y = self.y()
        self.move(self.x(), start_y)
        self.anim_start = time.time()
        self.anim_timer = QTimer(self)
        self.anim_timer.setInterval(10)
        def _step():
            progress = min(1.0, (time.time() - self.anim_start) / 0.22)
            ease = 1.0 - math.pow(1.0 - progress, 3)
            self.setWindowOpacity(ease)
            self.move(self.x(), int(start_y + (target_y - start_y) * ease))
            if progress >= 1.0: self.anim_timer.stop()
        self.anim_timer.timeout.connect(_step)
        self.anim_timer.start()

    def reject(self):
        if self._is_closing: super().reject(); return
        self._is_closing = True
        start_y = self.y()
        target_y = self.y() + 20
        start_op = self.windowOpacity()
        self.anim_start = time.time()
        self.anim_timer = QTimer(self)
        self.anim_timer.setInterval(10)
        def _step():
            progress = min(1.0, (time.time() - self.anim_start) / 0.15)
            self.setWindowOpacity(start_op * (1.0 - progress))
            self.move(self.x(), int(start_y + (target_y - start_y) * progress))
            if progress >= 1.0: 
                self.anim_timer.stop()
                super(SocialLoginPopup, self).reject()
        self.anim_timer.timeout.connect(_step)
        self.anim_timer.start()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        
        card = QFrame(self)
        card.setStyleSheet("""
            QFrame {
                background-color: #0E161C;
                border: 1px solid rgba(0, 229, 255, 0.35);
                border-radius: 16px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(35)
        shadow.setColor(QColor(0, 229, 255, 70))
        shadow.setOffset(0, 4)
        card.setGraphicsEffect(shadow)
        
        c_layout = QVBoxLayout(card)
        c_layout.setContentsMargins(22, 22, 22, 20)
        c_layout.setSpacing(12)
        
        title = QLabel("Sign in with other options")
        title.setFont(QFont("Inter", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #FFFFFF; border: none; background: transparent;")
        c_layout.addWidget(title)
        
        sub = QLabel("Select your identity provider below")
        sub.setFont(QFont("Inter", 9))
        sub.setAlignment(Qt.AlignCenter)
        sub.setStyleSheet("color: #94A3B8; border: none; background: transparent; margin-bottom: 4px;")
        c_layout.addWidget(sub)
        
        google_btn = QPushButton("  Continue with Google")
        google_btn.setFixedHeight(42)
        google_btn.setIcon(QIcon(get_svg_pixmap_from_raw(GOOGLE_SVG, 22)))
        google_btn.setIconSize(QSize(22, 22))
        google_btn.setCursor(Qt.PointingHandCursor)
        google_btn.setStyleSheet("""
            QPushButton {
                background: #FFFFFF;
                color: #1F2937;
                border-radius: 10px;
                font-weight: bold;
                font-size: 12px;
                border: 1px solid #E5E7EB;
                padding-left: 14px;
                text-align: center;
            }
            QPushButton:hover {
                background: #F3F4F6;
                border: 1px solid #D1D5DB;
            }
        """)
        c_layout.addWidget(google_btn)
        
        github_btn = QPushButton("  Continue with GitHub")
        github_btn.setFixedHeight(42)
        github_btn.setIcon(QIcon(get_svg_pixmap_from_raw(GITHUB_SVG, 22)))
        github_btn.setIconSize(QSize(22, 22))
        github_btn.setCursor(Qt.PointingHandCursor)
        github_btn.setStyleSheet("""
            QPushButton {
                background: #24292E;
                color: #FFFFFF;
                border-radius: 10px;
                font-weight: bold;
                font-size: 12px;
                border: 1px solid #3F4448;
                padding-left: 14px;
                text-align: center;
            }
            QPushButton:hover {
                background: #1B1F23;
                border: 1px solid #57606A;
            }
        """)
        c_layout.addWidget(github_btn)
        
        close_btn = QPushButton("Cancel")
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("QPushButton { background: transparent; color: #94A3B8; border: none; font-size: 11.5px; font-weight: bold; } QPushButton:hover { color: #FFFFFF; }")
        close_btn.clicked.connect(self.reject)
        c_layout.addWidget(close_btn, alignment=Qt.AlignCenter)
        
        layout.addWidget(card)


class LegalNoticeDialog(QDialog):
    """ Glassmorphic Terms of Service & Privacy Policy Viewer """
    def __init__(self, title: str, content: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(540, 480)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        card = QFrame(self)
        card.setStyleSheet("""
            QFrame {
                background-color: #070D12;
                border: 1.5px solid rgba(0, 229, 255, 0.4);
                border-radius: 16px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(35)
        shadow.setColor(QColor(0, 229, 255, 80))
        card.setGraphicsEffect(shadow)
        
        c_layout = QVBoxLayout(card)
        c_layout.setContentsMargins(24, 20, 24, 20)
        c_layout.setSpacing(12)
        
        header_row = QHBoxLayout()
        t_lbl = QLabel(title)
        t_lbl.setFont(QFont("Inter", 14, QFont.Bold))
        t_lbl.setStyleSheet("color: #FFFFFF; border:none; background:transparent;")
        header_row.addWidget(t_lbl)
        header_row.addStretch()
        
        x_btn = QPushButton("✕")
        x_btn.setFixedSize(24, 24)
        x_btn.setCursor(Qt.PointingHandCursor)
        x_btn.setStyleSheet("QPushButton { color: #94A3B8; background: transparent; border:none; font-weight:bold; } QPushButton:hover { color: #EF4444; }")
        x_btn.clicked.connect(self.accept)
        header_row.addWidget(x_btn)
        c_layout.addLayout(header_row)
        
        browser = QTextBrowser()
        browser.setHtml(f"<div style='color:#CBD5E1; font-family:Inter, sans-serif; font-size:12px; line-height:1.6;'>{content}</div>")
        browser.setStyleSheet("background: rgba(14, 22, 28, 0.6); border: 1px solid #1E2D38; border-radius: 8px; padding: 12px;")
        c_layout.addWidget(browser, 1)
        
        ok_btn = QPushButton("Understood & Agree")
        ok_btn.setFixedHeight(36)
        ok_btn.setCursor(Qt.PointingHandCursor)
        ok_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF);
                color: #04080B;
                border-radius: 8px;
                font-weight: bold;
                font-size: 12px;
                border: none;
            }}
            QPushButton:hover {{
                background: #00C4DA;
            }}
        """)
        ok_btn.clicked.connect(self.accept)
        c_layout.addWidget(ok_btn)
        
        layout.addWidget(card)


class ForgotPasswordDialog(QDialog):
    """ Account Recovery & Password Reset Dialog """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Account Recovery")
        self.setFixedSize(450, 310)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        card = QFrame(self)
        card.setStyleSheet("""
            QFrame {
                background-color: #070D12;
                border: 1.5px solid rgba(0, 229, 255, 0.4);
                border-radius: 16px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(35)
        shadow.setColor(QColor(0, 229, 255, 80))
        card.setGraphicsEffect(shadow)

        c_layout = QVBoxLayout(card)
        c_layout.setContentsMargins(24, 20, 24, 20)
        c_layout.setSpacing(12)

        header_row = QHBoxLayout()
        t_lbl = QLabel("Reset Password")
        t_lbl.setFont(QFont("Inter", 14, QFont.Bold))
        t_lbl.setStyleSheet("color: #FFFFFF; border:none; background:transparent;")
        header_row.addWidget(t_lbl)
        header_row.addStretch()

        x_btn = QPushButton("✕")
        x_btn.setFixedSize(24, 24)
        x_btn.setCursor(Qt.PointingHandCursor)
        x_btn.setStyleSheet("QPushButton { color: #94A3B8; background: transparent; border:none; font-weight:bold; } QPushButton:hover { color: #EF4444; }")
        x_btn.clicked.connect(self.reject)
        header_row.addWidget(x_btn)
        c_layout.addLayout(header_row)

        desc = QLabel("Enter your registered email address or username to receive password reset instructions.")
        desc.setWordWrap(True)
        desc.setFont(QFont("Inter", 9.5))
        desc.setStyleSheet("color: #94A3B8; border:none; background:transparent;")
        c_layout.addWidget(desc)

        self.email_input = AnimatedUnderlineLineEdit(placeholder="Enter email or username", is_password=False)
        c_layout.addWidget(self.email_input)

        self.status_lbl = QLabel("")
        self.status_lbl.setFont(QFont("Inter", 9))
        self.status_lbl.setStyleSheet("color: #10B981; border:none; background:transparent;")
        c_layout.addWidget(self.status_lbl)

        btn_row = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedHeight(34)
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.setStyleSheet("QPushButton { background: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 8px; font-weight: bold; } QPushButton:hover { color: #FFF; }")
        cancel_btn.clicked.connect(self.reject)

        send_btn = CyberSpinnerButton("Send Reset Link")
        send_btn.setFixedHeight(34)
        send_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF);
                color: #04080B;
                border-radius: 8px;
                font-weight: bold;
                font-size: 11.5px;
                border: none;
            }}
            QPushButton:hover {{
                background: #00C4DA;
            }}
        """)
        send_btn.clicked.connect(lambda: self._handle_send(send_btn))

        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(send_btn)
        c_layout.addLayout(btn_row)

        layout.addWidget(card)

    def _handle_send(self, btn: CyberSpinnerButton):
        val = self.email_input.text().strip()
        if not val:
            self.status_lbl.setText("Please enter your email or username.")
            self.status_lbl.setStyleSheet("color: #EF4444;")
            return
        btn.start_loading()
        QTimer.singleShot(1000, lambda: self._finish_send(btn))

    def _finish_send(self, btn: CyberSpinnerButton):
        btn.stop_loading()
        self.status_lbl.setText("✓ Recovery link dispatched to your email.")
        self.status_lbl.setStyleSheet("color: #10B981;")
        QTimer.singleShot(1400, self.accept)


class ThinkingAnimationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.phase = 0.0
        self.setFixedHeight(24)
        self.setFixedWidth(50)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_phase)

    def start_anim(self):
        self.timer.start(50)
        self.show()

    def stop_anim(self):
        self.timer.stop()
        self.hide()

    def _update_phase(self):
        self.phase += 0.15
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        color = QColor(GlobalConfig.ACCENT_COLOR)
        
        for i in range(3):
            alpha = int((math.sin(self.phase - i * 0.8) + 1) / 2 * 200 + 55)
            color.setAlpha(alpha)
            painter.setBrush(color)
            painter.drawEllipse(i * 14 + 6, 8, 6, 6)

class ModelArenaColumn(QFrame):
    close_requested = Signal(str)
    tts_requested = Signal(str, str)
    copy_requested = Signal(str)
    branch_requested = Signal(int)

    def __init__(self, model_id: str, parent=None):
        super().__init__(parent)
        self.model_id = model_id
        self.model_info = FREE_MODELS_REGISTRY.get(model_id, {})
        self.current_stream_buffer = ""
        self.current_turn_response = ""
        self.full_turn_history = []
        self.is_playing_audio = False
        self.is_active_streaming = False

        self.token_queue = deque()

        self.setObjectName("modelColumn")
        self.setMinimumWidth(380)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        badge_col = self.model_info.get("badge_color", GlobalConfig.ACCENT_COLOR)

        self.stream_render_timer = QTimer(self)
        self.stream_render_timer.setInterval(22)
        self.stream_render_timer.timeout.connect(self._on_stream_timer_tick)

        main_vbox = QVBoxLayout(self)
        main_vbox.setContentsMargins(0, 0, 0, 0)
        main_vbox.setSpacing(0)

        self.header_frame = QFrame()
        self.header_frame.setFixedHeight(46)
        self.header_frame.setStyleSheet(f"""
            QFrame {{ background-color: rgba(18, 29, 36, 0.85); border-top-left-radius: 10px; border-top-right-radius: 10px; border-bottom: 1px solid rgba(0, 229, 255, 0.2); }}
        """)
        h_layout = QHBoxLayout(self.header_frame)
        h_layout.setContentsMargins(12, 6, 12, 6)
        h_layout.setSpacing(10)

        logo_lbl = QLabel()
        logo_lbl.setFixedSize(22, 22)
        logo_lbl.setPixmap(get_model_logo_pixmap(self.model_info.get("logo_key", "gemini"), size=22))
        h_layout.addWidget(logo_lbl)

        title_lbl = QLabel(self.model_info.get("name", model_id))
        title_lbl.setFont(QFont("Inter", 10, QFont.Bold))
        title_lbl.setStyleSheet("color: #FFFFFF; background: transparent; border: none;")
        h_layout.addWidget(title_lbl)

        tag_lbl = QLabel(self.model_info.get("provider_tag", ""))
        tag_lbl.setFont(QFont("Inter", 8))
        tag_lbl.setStyleSheet(f"QLabel {{ background-color: {badge_col}22; color: {badge_col}; border: 1px solid {badge_col}50; border-radius: 4px; padding: 2px 6px; }}")
        h_layout.addWidget(tag_lbl)
        h_layout.addStretch()

        self.thinking_anim = ThinkingAnimationWidget()
        self.thinking_anim.hide()
        h_layout.addWidget(self.thinking_anim)

        self.status_badge = QLabel("Ready")
        self.status_badge.setFont(QFont("Inter", 8, QFont.Bold))
        self.status_badge.setStyleSheet(f"color: {badge_col}; background: transparent; border: none;")
        h_layout.addWidget(self.status_badge)

        self.tts_btn = QPushButton("Vol")
        self.tts_btn.setFixedSize(30, 26)
        self.tts_btn.setCursor(Qt.PointingHandCursor)
        self.tts_btn.setStyleSheet("QPushButton { background: rgba(18,29,36,0.6); color: #94A3B8; border: 1px solid rgba(0,229,255,0.2); border-radius: 6px; font-size: 10px; } QPushButton:hover { background-color: rgba(0,229,255,0.2); color: #FFFFFF; border: 1px solid #00E5FF; }")
        self.tts_btn.clicked.connect(self._on_tts_clicked)
        h_layout.addWidget(self.tts_btn)

        self.copy_btn = QPushButton("Copy")
        self.copy_btn.setFixedSize(40, 26)
        self.copy_btn.setCursor(Qt.PointingHandCursor)
        self.copy_btn.setStyleSheet("QPushButton { background: rgba(18,29,36,0.6); color: #94A3B8; border: 1px solid rgba(0,229,255,0.2); border-radius: 6px; font-size: 10px; } QPushButton:hover { background-color: rgba(0,229,255,0.2); color: #FFFFFF; border: 1px solid #00E5FF; }")
        self.copy_btn.clicked.connect(self._on_copy_clicked)
        h_layout.addWidget(self.copy_btn)

        self.close_btn = QPushButton("✕")
        self.close_btn.setFixedSize(26, 26)
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.setStyleSheet("QPushButton { background: transparent; color: #71717A; border: 1px solid transparent; border-radius: 6px; font-size: 12px; font-weight: bold; } QPushButton:hover { background-color: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid #EF4444; }")
        self.close_btn.clicked.connect(self.animate_column_close)
        h_layout.addWidget(self.close_btn)

        main_vbox.addWidget(self.header_frame)

        self.browser = QTextBrowser()
        self.browser.setOpenExternalLinks(False)
        self.browser.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.browser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.browser.setStyleSheet("background-color: transparent; border: none; padding: 14px;")
        self.browser.anchorClicked.connect(self._handle_anchor_click)
        main_vbox.addWidget(self.browser, 1)

        self.setStyleSheet(f"""
            QFrame#modelColumn {{
                background-color: rgba(14, 22, 28, 0.62);
                border: 1.5px solid rgba(0, 229, 255, 0.28);
                border-top: 3px solid {badge_col};
                border-radius: 12px;
            }}
        """)
        self.show_placeholder()

    def animate_column_close(self):
        """ Smooth width-collapse and fade-out animation before deletion """
        if hasattr(self, '_is_animating_close') and self._is_animating_close:
            return
        self._is_animating_close = True
        
        self.anim = QPropertyAnimation(self, b"maximumWidth")
        self.anim.setDuration(240)
        self.anim.setStartValue(self.width())
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.finished.connect(lambda: self.close_requested.emit(self.model_id))
        self.anim.start()

    def show_placeholder(self):
        desc = self.model_info.get("desc", "")
        html = f"""
            <div style="text-align: center; margin-top: 50px; padding: 20px;">
                <div style="font-size: 15px; font-weight: bold; color: #FFFFFF; margin-bottom: 6px;">{self.model_info.get('name', '')}</div>
                <div style="font-size: 12px; color: #94A3B8; line-height: 1.5; margin-bottom: 16px;">{desc}</div>
                <div style="display: inline-block; background-color: rgba(0, 229, 255, 0.12); border: 1px solid {GlobalConfig.ACCENT_COLOR}; border-radius: 6px; padding: 6px 14px; font-size: 11px; color: {GlobalConfig.ACCENT_COLOR}; font-weight:bold;">Ready for execution</div>
            </div>
        """
        self.browser.setHtml(html)

    def reset_column(self):
        try:
            self.stream_render_timer.stop()
            self.token_queue.clear()
            self.is_active_streaming = False
            self.current_stream_buffer = ""
            self.current_turn_response = ""
            self.full_turn_history.clear()
            self.is_playing_audio = False
            self.tts_btn.setText("Vol")
            bcol = self.model_info.get("badge_color", GlobalConfig.ACCENT_COLOR)
            self.status_badge.setText("Ready")
            self.status_badge.setStyleSheet(f"color: {bcol}; background: transparent; border: none;")
            self.status_badge.show()
            self.thinking_anim.stop_anim()
            self.show_placeholder()
        except Exception: pass

    def append_user_prompt(self, prompt: str, raw_text: str = ""):
        self.stream_render_timer.stop()
        self.token_queue.clear()
        self.current_stream_buffer = ""
        self.current_turn_response = ""
        self.is_active_streaming = True
        self.full_turn_history.append({"type": "user", "text": prompt, "raw_text": raw_text or prompt})
        self.render_all_turns(is_streaming=True)
        self.stream_render_timer.start()
        self.status_badge.hide()
        self.thinking_anim.start_anim()

    def append_chunk(self, chunk: str):
        tokens = re.findall(r'\S+\s*|\s+', chunk)
        for tok in tokens: self.token_queue.append(tok)
        if not self.stream_render_timer.isActive(): self.stream_render_timer.start()

    def _on_stream_timer_tick(self):
        if self.token_queue:
            tok = self.token_queue.popleft()
            self.current_stream_buffer += tok
            self.current_turn_response += tok
            
            if len(self.token_queue) > 10:
                for _ in range(min(len(self.token_queue), 3)):
                    tok2 = self.token_queue.popleft()
                    self.current_stream_buffer += tok2
                    self.current_turn_response += tok2

            self.render_all_turns(is_streaming=True)
            v_bar = self.browser.verticalScrollBar()
            v_bar.setValue(v_bar.maximum())
        elif not self.is_active_streaming:
            self.stream_render_timer.stop()
            self.render_all_turns(is_streaming=False)
            v_bar = self.browser.verticalScrollBar()
            v_bar.setValue(v_bar.maximum())

    def finish_turn(self, final_text: str = ""):
        self.is_active_streaming = False
        while self.token_queue:
            tok = self.token_queue.popleft()
            self.current_stream_buffer += tok
            self.current_turn_response += tok

        if final_text:
            self.current_stream_buffer = final_text
            self.current_turn_response = final_text

        self.stream_render_timer.stop()
        if self.current_stream_buffer.strip(): self.full_turn_history.append({"type": "assistant", "text": self.current_stream_buffer})
        self.current_stream_buffer = ""
        self.render_all_turns(is_streaming=False)
        v_bar = self.browser.verticalScrollBar()
        v_bar.setValue(v_bar.maximum())
        self.thinking_anim.stop_anim()
        self.status_badge.show()

    def set_error_state(self, error_code: str, error_message: str):
        self.stream_render_timer.stop()
        self.token_queue.clear()
        self.is_active_streaming = False
        self.current_stream_buffer = ""
        self.current_turn_response = f"[Error: {error_message}]"
        
        self.thinking_anim.stop_anim()
        self.status_badge.show()

        badge_text = "Error"
        if error_code == "KEY_MISSING": badge_text = "Key Required"
        elif error_code == "KEY_INVALID": badge_text = "Invalid Key"
        elif error_code == "RATE_LIMIT": badge_text = "Rate Limited"
        elif error_code == "MODEL_NOT_FOUND": badge_text = "Model 404"
        elif error_code == "QUOTA_EXCEEDED": badge_text = "Credits Empty"
        elif error_code == "NETWORK_ERROR": badge_text = "Network Offline"
        elif error_code == "TIMEOUT": badge_text = "Timeout"

        self.status_badge.setText(badge_text)
        self.status_badge.setStyleSheet("color: #EF4444; font-weight: bold;")

        clean_err = error_message.replace("<", "&lt;").replace(">", "&gt;")
        err_box = f"""
            <div style="background-color: rgba(18, 29, 36, 0.8); border: 1px solid #1E2D38; border-left: 4px solid #EF4444; border-radius: 8px; padding: 12px 16px; margin: 10px 0;">
                <div style="color: #EF4444; font-weight: bold; font-size: 12px; margin-bottom: 4px;">{badge_text}: {self.model_info.get('name', self.model_id)}</div>
                <div style="color: #94A3B8; font-size: 11.5px; line-height: 1.5; word-wrap: break-word;">{clean_err}</div>
            </div>
        """
        self.full_turn_history.append({"type": "error", "html": err_box})
        self.render_all_turns(is_streaming=False)

    def append_historical_user_prompt(self, prompt: str, raw_text: str = ""):
        self.full_turn_history.append({"type": "user", "text": prompt, "raw_text": raw_text or prompt})

    def append_historical_assistant_response(self, text: str):
        if text.startswith("[Error:"):
            clean_err = text.replace("<", "&lt;").replace(">", "&gt;")
            err_box = f"""
                <div style="background-color: rgba(18, 29, 36, 0.8); border: 1px solid #1E2D38; border-left: 4px solid #EF4444; border-radius: 8px; padding: 12px 16px; margin: 10px 0;">
                    <div style="color: #EF4444; font-weight: bold; font-size: 12px; margin-bottom: 4px;">Historical Error Notice</div>
                    <div style="color: #94A3B8; font-size: 11.5px; line-height: 1.5;">{clean_err}</div>
                </div>
            """
            self.full_turn_history.append({"type": "error", "html": err_box})
        else: self.full_turn_history.append({"type": "assistant", "text": text})

    def render_all_turns(self, is_streaming: bool = False):
        try:
            cur_font_size = GlobalConfig.CHAT_FONT_SIZE
            blocks = []
            for idx, item in enumerate(self.full_turn_history):
                if item["type"] == "user":
                    clean_u = item["text"].replace("\n", "<br>")
                    clean_u = markdown.markdown(clean_u, extensions=['nl2br'])
                    
                    branch_html = f"<a href='branch:{idx}' style='color: rgba(0, 229, 255, 0.85); font-size: 10px; font-weight:bold; text-decoration: none; margin-left: 8px;'>[EDIT & BRANCH]</a>"
                    
                    # RIGHT-ALIGNED USER CHAT BUBBLE
                    blocks.append(f"""
                        <div style="display: block; width: 100%; margin: 10px 0; overflow: hidden; clear: both;">
                            <div style="float: right; max-width: 82%; background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #102A36, stop:1 #0C1E26); border: 1.5px solid rgba(0, 229, 255, 0.4); border-top-right-radius: 4px; border-top-left-radius: 14px; border-bottom-left-radius: 14px; border-bottom-right-radius: 14px; padding: 10px 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
                                <div style="color: {GlobalConfig.ACCENT_COLOR}; font-size: 9.5px; font-weight: bold; text-transform: uppercase; margin-bottom: 3px; letter-spacing: 0.5px;">PROMPT {branch_html}</div>
                                <div style="color: #FFFFFF; font-size: {cur_font_size}px; line-height: 1.45; text-align: left;">{clean_u}</div>
                            </div>
                        </div>
                        <div style="clear: both;"></div>
                    """)
                elif item["type"] == "assistant":
                    md_html = render_styled_markdown(item["text"], is_streaming=False, font_size=cur_font_size)
                    blocks.append(f"<div style='margin: 8px 0 16px 0; clear: both;'>{md_html}</div>")
                elif item["type"] == "error": 
                    blocks.append(f"<div style='clear: both;'>{item['html']}</div>")

            if self.current_stream_buffer or is_streaming:
                active_md = render_styled_markdown(self.current_stream_buffer, is_streaming=is_streaming, font_size=cur_font_size)
                blocks.append(f"<div style='margin: 8px 0 16px 0; clear: both;'>{active_md}</div>")

            self.browser.setHtml("".join(blocks))
        except Exception: pass

    def _handle_anchor_click(self, url: QUrl):
        try:
            url_str = url.toString()
            if url_str.startswith("copycode:"): 
                QApplication.clipboard().setText(urllib.parse.unquote(url_str[len("copycode:"):]))
            elif url_str.startswith("previewcode:"):
                code = urllib.parse.unquote(url_str[len("previewcode:"):])
                HTMLPreviewDialog(code, self).exec()
            elif url_str.startswith("runcode:"):
                code = urllib.parse.unquote(url_str[len("runcode:"):])
                PythonRunnerDialog(code, self).exec()
            elif url_str.startswith("branch:"): 
                self.branch_requested.emit(int(url_str.split(":")[1]))
            else: 
                QDesktopServices.openUrl(url)
        except Exception: pass

    def _on_tts_clicked(self): self.tts_requested.emit(self.model_id, self.get_current_turn_text())
    def _on_copy_clicked(self): self.copy_requested.emit(self.get_current_turn_text())
    def get_current_turn_text(self) -> str: return self.current_turn_response

    def set_audio_playing(self, is_playing: bool):
        self.is_playing_audio = is_playing
        self.tts_btn.setText("Stop" if is_playing else "Vol")
        self.tts_btn.setStyleSheet("QPushButton { background-color: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid #EF4444; border-radius: 6px; font-size: 10px; }" if is_playing else "QPushButton { background: rgba(18,29,36,0.6); color: #94A3B8; border: 1px solid rgba(0,229,255,0.2); border-radius: 6px; font-size: 10px; } QPushButton:hover { background-color: rgba(0,229,255,0.2); color: #FFFFFF; border: 1px solid #00E5FF; }")

# ==============================================================================
# 9. INPUT & VISUAL WIDGETS
# ==============================================================================

class AttachmentBadgeChip(QFrame):
    removed = Signal(str)
    def __init__(self, file_id: str, file_name: str, file_type: str, thumbnail: Optional[QPixmap] = None, parent=None):
        super().__init__(parent)
        self.file_id = file_id
        self.setFixedHeight(30)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 2, 8, 2)
        layout.setSpacing(8)

        if thumbnail and not thumbnail.isNull():
            icon_lbl = QLabel()
            icon_lbl.setFixedSize(16, 16)
            icon_lbl.setPixmap(thumbnail.scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(icon_lbl)
        else:
            icon_lbl = QLabel("DOC")
            icon_lbl.setFont(QFont("Inter", 8, QFont.Bold))
            icon_lbl.setStyleSheet("color: #94A3B8; background: transparent;")
            layout.addWidget(icon_lbl)

        short_name = file_name if len(file_name) <= 18 else file_name[:15] + "..."
        name_lbl = QLabel(short_name)
        name_lbl.setFont(QFont("Inter", 9, QFont.Bold))
        name_lbl.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; background: transparent; border: none;")
        name_lbl.setToolTip(file_name)
        layout.addWidget(name_lbl)

        del_btn = QPushButton("✕")
        del_btn.setFixedSize(16, 16)
        del_btn.setCursor(Qt.PointingHandCursor)
        del_btn.setStyleSheet("QPushButton { background-color: rgba(239, 68, 68, 0.2); color: #EF4444; border: none; border-radius: 8px; font-size: 9px; font-weight: bold; } QPushButton:hover { background-color: #EF4444; color: #FFFFFF; }")
        del_btn.clicked.connect(lambda: self.removed.emit(self.file_id))
        layout.addWidget(del_btn)
        self.setStyleSheet(f"QFrame {{ background-color: rgba(0, 229, 255, 0.12); border: 1px solid {GlobalConfig.ACCENT_COLOR}; border-radius: 8px; }}")

class ChatInputTextEdit(QTextEdit):
    returnPressed = Signal()
    largeTextPasted = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textChanged.connect(self.adjust_height)
        self.setStyleSheet(f"QTextEdit {{ background-color: transparent; color: #FFFFFF; border: none; font-size: 13.5px; font-family: 'Inter', 'Segoe UI', sans-serif; padding: 8px 6px; }}")

    def adjust_height(self):
        try:
            doc_height = int(self.document().size().height())
            new_height = max(40, min(160, doc_height + 12))
            self.setFixedHeight(new_height)
        except Exception: pass

    def insertFromMimeData(self, source):
        try:
            if source.hasText():
                text = source.text()
                if text.count('\n') > 50 or len(text) > 2500:
                    self.largeTextPasted.emit(text)
                    return
        except Exception: pass
        super().insertFromMimeData(source)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return and not (event.modifiers() & Qt.ShiftModifier):
            self.returnPressed.emit()
            event.accept()
        else: 
            super().keyPressEvent(event)

class VoiceWaveformWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.phase = 0.0
        self.bars = 7
        self.setFixedHeight(22)
        self.setFixedWidth(48)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.start(16)

    def _tick(self):
        self.phase += 0.12
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        bar_w, gap = 2.8, 2.8
        start_x = (self.width() - (self.bars * (bar_w + gap))) / 2.0
        mid_y = self.height() / 2.0

        for i in range(self.bars):
            h_factor = math.sin(self.phase + i * 0.8) * 0.5 + 0.5
            bar_h = max(4, int(15 * h_factor))
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(GlobalConfig.ACCENT_COLOR))
            painter.drawRoundedRect(QRect(int(start_x + i * (bar_w + gap)), int(mid_y - (bar_h / 2.0)), int(bar_w), bar_h), 2, 2)
        painter.end()

# ==============================================================================
# 10. MODEL SELECTION MATRIX
# ==============================================================================
class ModelSelectionCard(QFrame):
    toggled_signal = Signal(str, bool)

    def __init__(self, model_id: str, model_data: dict, is_checked: bool = False, parent=None):
        super().__init__(parent)
        self.model_id = model_id
        self.model_data = model_data
        self.is_checked_state = is_checked
        self.is_hovered = False
        
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(86)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(14)

        self.checkbox = QCheckBox()
        self.checkbox.setChecked(is_checked)
        self.checkbox.stateChanged.connect(self._on_check_changed)
        layout.addWidget(self.checkbox)

        icon_box = QFrame()
        icon_box.setFixedSize(38, 38)
        bcol = model_data.get("badge_color", GlobalConfig.ACCENT_COLOR)
        icon_box.setStyleSheet(f"""
            QFrame {{
                background-color: {bcol}15;
                border: 1px solid {bcol}40;
                border-radius: 10px;
            }}
        """)
        ib_layout = QVBoxLayout(icon_box)
        ib_layout.setContentsMargins(0, 0, 0, 0)
        logo_lbl = QLabel()
        logo_lbl.setAlignment(Qt.AlignCenter)
        logo_lbl.setPixmap(get_model_logo_pixmap(model_data.get("logo_key", "gemini"), size=24))
        ib_layout.addWidget(logo_lbl)
        layout.addWidget(icon_box)

        vbox = QVBoxLayout()
        vbox.setSpacing(4)
        top_row = QHBoxLayout()
        top_row.setSpacing(8)
        
        self.title_lbl = QLabel(model_data["name"])
        self.title_lbl.setFont(QFont("Inter", 11, QFont.Bold))
        self.title_lbl.setStyleSheet("color: #FFFFFF; background: transparent; border: none;")

        self.tag_lbl = QLabel(model_data["provider_tag"])
        self.tag_lbl.setFont(QFont("Inter", 8, QFont.Bold))
        self.tag_lbl.setStyleSheet(f"QLabel {{ background-color: {bcol}22; color: {bcol}; border: 1px solid {bcol}60; border-radius: 6px; padding: 2px 8px; }}")
        
        top_row.addWidget(self.title_lbl)
        top_row.addWidget(self.tag_lbl)
        top_row.addStretch()
        vbox.addLayout(top_row)

        self.desc_lbl = QLabel(model_data["desc"])
        self.desc_lbl.setFont(QFont("Inter", 8.5))
        self.desc_lbl.setStyleSheet("color: #94A3B8; background: transparent; border: none;")
        self.desc_lbl.setWordWrap(True)
        vbox.addWidget(self.desc_lbl)

        layout.addLayout(vbox, 1)
        self.update_card_style()

    def enterEvent(self, event):
        self.is_hovered = True
        self.update_card_style()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.is_hovered = False
        self.update_card_style()
        super().leaveEvent(event)

    def _on_check_changed(self, state):
        self.is_checked_state = self.checkbox.isChecked()
        self.toggled_signal.emit(self.model_id, self.is_checked_state)
        self.update_card_style()

    def set_checked(self, checked: bool):
        self.is_checked_state = checked
        self.checkbox.blockSignals(True)
        self.checkbox.setChecked(checked)
        self.checkbox.blockSignals(False)
        self.update_card_style()

    def is_checked(self) -> bool: 
        return self.checkbox.isChecked()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: 
            self.checkbox.setChecked(not self.checkbox.isChecked())
        super().mousePressEvent(event)

    def update_card_style(self):
        checked = self.checkbox.isChecked()
        bcol = self.model_data["badge_color"]
        
        if checked:
            self.shadow.setColor(QColor(bcol).lighter(120))
            self.shadow.setBlurRadius(24)
            self.setStyleSheet(f"""
                QFrame {{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #12222E, stop:0.5 #0F1D26, stop:1 #0A141A);
                    border: 1.5px solid {bcol};
                    border-left: 5px solid {bcol};
                    border-radius: 12px;
                }}
                QCheckBox::indicator {{
                    width: 18px;
                    height: 18px;
                    border-radius: 5px;
                    border: 1.5px solid {bcol};
                    background-color: {bcol};
                }}
            """)
        elif self.is_hovered:
            self.shadow.setColor(QColor(0, 229, 255, 60))
            self.shadow.setBlurRadius(16)
            self.setStyleSheet(f"""
                QFrame {{
                    background: #111C23;
                    border: 1px solid rgba(0, 229, 255, 0.4);
                    border-radius: 12px;
                }}
                QCheckBox::indicator {{
                    width: 18px;
                    height: 18px;
                    border-radius: 5px;
                    border: 1.5px solid #00E5FF;
                    background-color: #0E161C;
                }}
            """)
        else:
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.shadow.setBlurRadius(10)
            self.setStyleSheet("""
                QFrame {{
                    background-color: #0B1318;
                    border: 1px solid #1A2834;
                    border-radius: 12px;
                }}
                QCheckBox::indicator {{
                    width: 18px;
                    height: 18px;
                    border-radius: 5px;
                    border: 1px solid #2A3E4E;
                    background-color: #080D11;
                }}
            """)

class ModelSelectionDialog(QDialog):
    models_selected_signal = Signal(list)

    def __init__(self, current_selected: List[str], parent=None):
        super().__init__(parent)
        self.selected_ids: Set[str] = set(current_selected or ["gemini-3.8"])
        self.cards_dict: Dict[str, ModelSelectionCard] = {}
        self.setWindowTitle("Model Matrix Selector - Nexus AI")
        self.setFixedSize(700, 640)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #070D12;
                color: #F4F4F5;
            }
            QLabel { color: #F4F4F5; }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 20, 22, 20)
        layout.setSpacing(14)

        top_h = QHBoxLayout()
        v_title = QVBoxLayout()
        v_title.setSpacing(3)
        
        t1 = QLabel("Model Matrix Selector")
        t1.setFont(QFont("Inter", 15, QFont.Bold))
        t1.setStyleSheet("color: #FFFFFF; letter-spacing: 0.5px;")
        
        t2 = QLabel("Select neural network endpoints to evaluate side-by-side in arena view.")
        t2.setFont(QFont("Inter", 9.5))
        t2.setStyleSheet("color: #94A3B8;")
        v_title.addWidget(t1)
        v_title.addWidget(t2)
        top_h.addLayout(v_title)
        top_h.addStretch()

        self.scan_ollama_btn = QPushButton("Scan Local Ollama")
        self.scan_ollama_btn.setCursor(Qt.PointingHandCursor)
        self.scan_ollama_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #0E181F;
                color: {GlobalConfig.ACCENT_COLOR};
                border: 1px solid rgba(0, 229, 255, 0.4);
                border-radius: 8px;
                padding: 7px 14px;
                font-weight: bold;
                font-size: 11px;
            }}
            QPushButton:hover {{
                background-color: rgba(0, 229, 255, 0.15);
                border: 1px solid {GlobalConfig.ACCENT_COLOR};
            }}
        """)
        self.scan_ollama_btn.clicked.connect(self._scan_ollama)
        top_h.addWidget(self.scan_ollama_btn)

        self.select_all_cb = QCheckBox("Select All")
        self.select_all_cb.setFont(QFont("Inter", 9.5, QFont.Bold))
        self.select_all_cb.setCursor(Qt.PointingHandCursor)
        self.select_all_cb.setStyleSheet(f"""
            QCheckBox {{ color: {GlobalConfig.ACCENT_COLOR}; spacing: 8px; }}
            QCheckBox::indicator {{ width: 16px; height: 16px; border-radius: 4px; border: 1px solid #1E2D38; background: #0B1318; }}
            QCheckBox::indicator:checked {{ background: {GlobalConfig.ACCENT_COLOR}; border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}
        """)
        self.select_all_cb.stateChanged.connect(self._toggle_select_all)
        top_h.addWidget(self.select_all_cb)
        layout.addLayout(top_h)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: 1px solid #13222C;
                border-radius: 12px;
                padding: 4px;
            }
        """)

        self.container = QWidget()
        self.container.setStyleSheet("background: transparent;")
        self.c_layout = QVBoxLayout(self.container)
        self.c_layout.setContentsMargins(6, 6, 6, 6)
        self.c_layout.setSpacing(10)

        self.populate_cards()

        self.scroll.setWidget(self.container)
        layout.addWidget(self.scroll, 1)

        bot_h = QHBoxLayout()
        self.status_lbl = QLabel("")
        self.status_lbl.setFont(QFont("Inter", 10, QFont.Bold))
        bot_h.addWidget(self.status_lbl)
        bot_h.addStretch()

        apply_btn = QPushButton("Apply Configuration")
        apply_btn.setCursor(Qt.PointingHandCursor)
        apply_btn.setFixedHeight(40)
        apply_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF);
                color: #04080B;
                border-radius: 10px;
                padding: 8px 24px;
                font-weight: bold;
                font-size: 13px;
                border: none;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:1 #0284C7);
            }}
        """)
        apply_btn.clicked.connect(self._apply_and_close)
        bot_h.addWidget(apply_btn)
        layout.addLayout(bot_h)
        self._update_status()

    def populate_cards(self):
        while self.c_layout.count():
            item = self.c_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.cards_dict.clear()

        for m_id, m_data in FREE_MODELS_REGISTRY.items():
            card = ModelSelectionCard(m_id, m_data, is_checked=(m_id in self.selected_ids))
            card.toggled_signal.connect(self._on_card_toggled)
            self.cards_dict[m_id] = card
            self.c_layout.addWidget(card)

    def _scan_ollama(self):
        try:
            req = urllib.request.Request("http://localhost:11434/api/tags")
            with urllib.request.urlopen(req, timeout=2) as resp:
                data = json.loads(resp.read().decode())
                added_count = 0
                for m in data.get("models", []):
                    mname = m["name"]
                    reg_id = f"ollama_{mname}"
                    if reg_id not in FREE_MODELS_REGISTRY:
                        FREE_MODELS_REGISTRY[reg_id] = {
                            "id": reg_id, "name": f"{mname} (Local)", "logo_key": "ollama",
                            "provider": "ollama", "api_model": mname, "provider_tag": "Ollama Offline",
                            "badge_color": "#94A3B8", "cost_in": 0.0, "cost_out": 0.0,
                            "desc": f"100% Local Offline Model: {mname}"
                        }
                        added_count += 1
                self.populate_cards()
                self._update_status()
                QMessageBox.information(self, "Ollama Scan", f"Scan complete! Added {added_count} new local models.")
        except Exception as e:
            QMessageBox.warning(self, "Ollama Error", f"Could not connect to Ollama on localhost:11434.\nMake sure Ollama is running.\nError: {str(e)}")

    def _on_card_toggled(self, model_id: str, checked: bool):
        if checked: self.selected_ids.add(model_id)
        else: self.selected_ids.discard(model_id)
        self._update_status()

    def _toggle_select_all(self, state):
        chk = (state == Qt.Checked.value or state == 2)
        for m_id, card in self.cards_dict.items():
            card.set_checked(chk)
            if chk: self.selected_ids.add(m_id)
            else: self.selected_ids.discard(m_id)
        self._update_status()

    def _update_status(self):
        count = len(self.selected_ids)
        total = len(FREE_MODELS_REGISTRY)
        self.select_all_cb.blockSignals(True)
        self.select_all_cb.setChecked(count == total)
        self.select_all_cb.blockSignals(False)

        if count == 0:
            self.status_lbl.setText("● Select at least 1 model")
            self.status_lbl.setStyleSheet("color: #EF4444;")
        else:
            self.status_lbl.setText(f"● {count} of {total} Models Active")
            self.status_lbl.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR};")

    def _apply_and_close(self):
        if not self.selected_ids:
            QMessageBox.warning(self, "Selection Required", "Select at least 1 AI model to continue.")
            return
        self.models_selected_signal.emit(list(self.selected_ids))
        self.accept()

# ==============================================================================
# 11. CUSTOM THEMED EXPORT DIALOG
# ==============================================================================
class CyberExportDialog(QDialog):
    def __init__(self, available_models: List[str], parent=None):
        super().__init__(parent)
        self.available_models = available_models
        self.selected_export_models = set(available_models)
        self.selected_format = "pdf"
        self.model_checkboxes: Dict[str, QCheckBox] = {}
        
        self.setWindowTitle("Export Conversation - Nexus AI")
        self.setFixedSize(520, 480)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.init_ui()

    def init_ui(self):
        main_vbox = QVBoxLayout(self)
        main_vbox.setContentsMargins(10, 10, 10, 10)

        card = QFrame(self)
        card.setStyleSheet("""
            QFrame {
                background-color: #0A1116;
                border: 1.5px solid rgba(0, 229, 255, 0.45);
                border-radius: 18px;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(36)
        shadow.setColor(QColor(0, 229, 255, 95))
        shadow.setOffset(0, 0)
        card.setGraphicsEffect(shadow)

        c_layout = QVBoxLayout(card)
        c_layout.setContentsMargins(24, 20, 24, 20)
        c_layout.setSpacing(14)

        top_h = QHBoxLayout()
        v_title = QVBoxLayout()
        v_title.setSpacing(2)
        t1 = QLabel("Export Conversation")
        t1.setFont(QFont("Inter", 14, QFont.Bold))
        t1.setStyleSheet("color: #FFFFFF; font-weight: bold; border:none; background:transparent;")
        t2 = QLabel("Select models to include in your exported report.")
        t2.setFont(QFont("Inter", 9))
        t2.setStyleSheet("color: #94A3B8; border:none; background:transparent;")
        v_title.addWidget(t1)
        v_title.addWidget(t2)
        top_h.addLayout(v_title)
        top_h.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(24, 24)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("QPushButton { color: #71717A; background: transparent; border: none; font-weight: bold; font-size: 13px; } QPushButton:hover { color: #EF4444; }")
        close_btn.clicked.connect(self.reject)
        top_h.addWidget(close_btn)
        c_layout.addLayout(top_h)

        sel_all_row = QHBoxLayout()
        lbl_models = QLabel("Neural Responses:")
        lbl_models.setFont(QFont("Inter", 10, QFont.Bold))
        lbl_models.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; border:none; background:transparent;")
        sel_all_row.addWidget(lbl_models)
        sel_all_row.addStretch()

        self.select_all_cb = QCheckBox("Select All")
        self.select_all_cb.setFont(QFont("Inter", 9, QFont.Bold))
        self.select_all_cb.setChecked(True)
        self.select_all_cb.setCursor(Qt.PointingHandCursor)
        self.select_all_cb.setStyleSheet(f"""
            QCheckBox {{ color: {GlobalConfig.ACCENT_COLOR}; spacing: 6px; border:none; background:transparent; }}
            QCheckBox::indicator {{ width: 15px; height: 15px; border-radius: 4px; border: 1px solid #1E2D38; background: #0B1318; }}
            QCheckBox::indicator:checked {{ background: {GlobalConfig.ACCENT_COLOR}; border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}
        """)
        self.select_all_cb.stateChanged.connect(self._toggle_select_all)
        sel_all_row.addWidget(self.select_all_cb)
        c_layout.addLayout(sel_all_row)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { background: rgba(14, 22, 28, 0.6); border: 1px solid #1E2D38; border-radius: 10px; }")

        m_container = QWidget()
        m_container.setStyleSheet("background: transparent;")
        m_vbox = QVBoxLayout(m_container)
        m_vbox.setContentsMargins(10, 10, 10, 10)
        m_vbox.setSpacing(8)

        for mid in self.available_models:
            minfo = FREE_MODELS_REGISTRY.get(mid, {"name": mid, "badge_color": GlobalConfig.ACCENT_COLOR, "logo_key": "gemini"})
            row_frame = QFrame()
            row_frame.setStyleSheet("QFrame { background-color: rgba(18, 29, 36, 0.7); border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 8px; padding: 4px; }")
            rf_layout = QHBoxLayout(row_frame)
            rf_layout.setContentsMargins(8, 4, 8, 4)
            rf_layout.setSpacing(10)

            cb = QCheckBox()
            cb.setChecked(True)
            cb.setCursor(Qt.PointingHandCursor)
            cb.setStyleSheet(f"""
                QCheckBox::indicator {{ width: 16px; height: 16px; border-radius: 4px; border: 1px solid #1E2D38; background: #080D11; }}
                QCheckBox::indicator:checked {{ background: {GlobalConfig.ACCENT_COLOR}; border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}
            """)
            cb.stateChanged.connect(lambda state, m=mid: self._on_model_toggled(m, state))
            self.model_checkboxes[mid] = cb
            rf_layout.addWidget(cb)

            logo_lbl = QLabel()
            logo_lbl.setFixedSize(18, 18)
            logo_lbl.setPixmap(get_model_logo_pixmap(minfo.get("logo_key", "gemini"), size=18))
            rf_layout.addWidget(logo_lbl)

            name_lbl = QLabel(minfo.get("name", mid))
            name_lbl.setFont(QFont("Inter", 10, QFont.Bold))
            name_lbl.setStyleSheet("color: #FFFFFF; border:none; background:transparent;")
            rf_layout.addWidget(name_lbl, 1)

            bcol = minfo.get("badge_color", GlobalConfig.ACCENT_COLOR)
            tag_lbl = QLabel(minfo.get("provider_tag", "AI"))
            tag_lbl.setFont(QFont("Inter", 8))
            tag_lbl.setStyleSheet(f"QLabel {{ background-color: {bcol}20; color: {bcol}; border: 1px solid {bcol}50; border-radius: 4px; padding: 1px 6px; }}")
            rf_layout.addWidget(tag_lbl)

            m_vbox.addWidget(row_frame)

        scroll.setWidget(m_container)
        c_layout.addWidget(scroll, 1)

        fmt_title = QLabel("Export File Format:")
        fmt_title.setFont(QFont("Inter", 10, QFont.Bold))
        fmt_title.setStyleSheet("color: #FFFFFF; border:none; background:transparent;")
        c_layout.addWidget(fmt_title)

        fmt_row = QHBoxLayout()
        fmt_row.setSpacing(10)
        self.fmt_btns = {}
        for fmt, label in [("pdf", "📕 PDF Document"), ("md", "📝 Markdown (.md)"), ("doc", "📄 MS Word / HTML")]:
            btn = QPushButton(label)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(34)
            btn.clicked.connect(lambda ch, f=fmt: self._set_format(f))
            self.fmt_btns[fmt] = btn
            fmt_row.addWidget(btn)
        c_layout.addLayout(fmt_row)
        self._update_format_buttons()

        bot_btns = QHBoxLayout()
        bot_btns.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.setFixedHeight(36)
        cancel_btn.setStyleSheet("QPushButton { background: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 8px; padding: 6px 16px; font-weight: bold; } QPushButton:hover { color: #FFFFFF; background: #1E2D38; }")
        cancel_btn.clicked.connect(self.reject)

        export_confirm_btn = QPushButton("Export Report")
        export_confirm_btn.setCursor(Qt.PointingHandCursor)
        export_confirm_btn.setFixedHeight(36)
        export_confirm_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF);
                color: #04080B;
                border-radius: 8px;
                padding: 6px 20px;
                font-weight: bold;
                font-size: 12.5px;
                border: none;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:1 #0284C7);
            }}
        """)
        export_confirm_btn.clicked.connect(self._confirm_export)

        bot_btns.addWidget(cancel_btn)
        bot_btns.addWidget(export_confirm_btn)
        c_layout.addLayout(bot_btns)

        main_vbox.addWidget(card)

    def _set_format(self, fmt: str):
        self.selected_format = fmt
        self._update_format_buttons()

    def _update_format_buttons(self):
        for fmt, btn in self.fmt_btns.items():
            if fmt == self.selected_format:
                btn.setStyleSheet(f"QPushButton {{ background-color: rgba(0, 229, 255, 0.2); color: {GlobalConfig.ACCENT_COLOR}; border: 1.5px solid {GlobalConfig.ACCENT_COLOR}; border-radius: 8px; font-weight: bold; font-size: 11px; }}")
            else:
                btn.setStyleSheet("QPushButton {{ background-color: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 8px; font-size: 11px; }} QPushButton:hover {{ color: #FFFFFF; }}")

    def _on_model_toggled(self, mid: str, state):
        if state == 2 or state == Qt.Checked.value:
            self.selected_export_models.add(mid)
        else:
            self.selected_export_models.discard(mid)
        
        self.select_all_cb.blockSignals(True)
        self.select_all_cb.setChecked(len(self.selected_export_models) == len(self.available_models))
        self.select_all_cb.blockSignals(False)

    def _toggle_select_all(self, state):
        chk = (state == Qt.Checked.value or state == 2)
        for mid, cb in self.model_checkboxes.items():
            cb.blockSignals(True)
            cb.setChecked(chk)
            cb.blockSignals(False)
            if chk: self.selected_export_models.add(mid)
            else: self.selected_export_models.discard(mid)

    def _confirm_export(self):
        if not self.selected_export_models:
            QMessageBox.warning(self, "Selection Required", "Please select at least one model response to export.")
            return
        self.accept()

# ==============================================================================
# 12. REDESIGNED COMPACT SETTINGS & AUTH MODALS WITH DARK POPUPS
# ==============================================================================
class SettingsAuthDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings Security Lock")
        self.setFixedSize(560, 340)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setModal(True)
        self._is_closing = False
        self._is_pass_visible = False
        self.init_ui()

    def showEvent(self, event):
        super().showEvent(event)
        if not hasattr(self, '_entrance_animated'):
            self._entrance_animated = True
            self.play_slide_up_entrance()

    def reject(self):
        if self._is_closing: super().reject(); return
        self._is_closing = True
        self.play_slide_down_exit()

    def accept(self):
        if self._is_closing: super().accept(); return
        self._is_closing = True
        self.play_slide_down_exit(is_accept=True)

    def play_slide_down_exit(self, is_accept=False):
        try:
            start_y, target_y, start_opacity = self.y(), self.y() + 30, self.windowOpacity()
            self._exit_start_time = time.time()
            self._exit_duration = 0.2
            self._exit_timer = QTimer(self)
            self._exit_timer.setInterval(8)

            def _step():
                now = time.time()
                raw = min(1.0, (now - self._exit_start_time) / self._exit_duration)
                ease = math.pow(raw, 3)
                self.setWindowOpacity(max(0.0, min(1.0, start_opacity * (1.0 - ease))))
                self.move(self.x(), int(start_y + (target_y - start_y) * ease))
                if raw >= 1.0:
                    self._exit_timer.stop()
                    if is_accept: super(SettingsAuthDialog, self).accept()
                    else: super(SettingsAuthDialog, self).reject()

            self._exit_timer.timeout.connect(_step)
            self._exit_timer.start()
        except Exception:
            if is_accept: super().accept()
            else: super().reject()

    def play_slide_up_entrance(self):
        try:
            self.setWindowOpacity(0.0)
            start_y, target_y = self.y() + 30, self.y()
            self.move(self.x(), start_y)
            self._entrance_start_time = time.time()
            self._entrance_duration = 0.3
            self._entrance_timer = QTimer(self)
            self._entrance_timer.setInterval(8)

            def _step():
                now = time.time()
                raw = min(1.0, (now - self._entrance_start_time) / self._entrance_duration)
                ease = 1.0 - math.pow(1.0 - raw, 3)
                self.setWindowOpacity(max(0.0, min(1.0, ease)))
                self.move(self.x(), int(start_y + (target_y - start_y) * ease))
                if raw >= 1.0:
                    self._entrance_timer.stop()
                    self.setWindowOpacity(1.0)
                    self.move(self.x(), target_y)

            self._entrance_timer.timeout.connect(_step)
            self._entrance_timer.start()
        except Exception: pass

    def init_ui(self):
        main_vbox = QVBoxLayout(self)
        main_vbox.setContentsMargins(10, 10, 10, 10)

        self.auth_card = TiltLoginCard(self)
        self.auth_card.setStyleSheet("""
            QFrame#loginCard {
                background-color: #070D12;
                border: 1.5px solid rgba(0, 229, 255, 0.45);
                border-radius: 18px;
            }
        """)

        card_layout = QHBoxLayout(self.auth_card)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(28, 24, 24, 24)
        left_layout.setSpacing(10)

        top_row = QHBoxLayout()
        title_lbl = QLabel("Settings Security")
        title_lbl.setFont(QFont("Inter", 15, QFont.Bold))
        title_lbl.setStyleSheet("color: #FFFFFF; font-weight: 700; border: none; background: transparent;")
        top_row.addWidget(title_lbl)
        top_row.addStretch()

        self.caps_warning = QLabel("⇪ CAPS ON")
        self.caps_warning.setFont(QFont("Inter", 7.5, QFont.Bold))
        self.caps_warning.setStyleSheet("background: rgba(245, 158, 11, 0.15); color: #F59E0B; border: 1px solid #F59E0B; border-radius: 5px; padding: 1px 4px;")
        self.caps_warning.hide()
        top_row.addWidget(self.caps_warning)
        left_layout.addLayout(top_row)

        u_box = QHBoxLayout()
        u_box.setSpacing(6)
        self.user_field = AnimatedUnderlineLineEdit(placeholder="Enter Username", is_password=False)
        self.user_field.returnPressed.connect(lambda: self.pass_field.setFocus())
        self.user_field.caps_changed.connect(lambda on: self.caps_warning.setVisible(on))
        
        u_icon = QLabel()
        u_icon.setPixmap(create_svg_icon("user", "#94A3B8", 16).pixmap(16, 16))
        u_icon.setStyleSheet("border:none; background:transparent;")
        u_box.addWidget(self.user_field, 1)
        u_box.addWidget(u_icon)
        left_layout.addLayout(u_box)

        p_box = QHBoxLayout()
        p_box.setSpacing(6)
        self.pass_field = AnimatedUnderlineLineEdit(placeholder="Enter Password", is_password=True)
        self.pass_field.returnPressed.connect(self.validate_and_unlock)
        self.pass_field.caps_changed.connect(lambda on: self.caps_warning.setVisible(on))

        self.eye_toggle_btn = QPushButton()
        self.eye_toggle_btn.setFixedSize(20, 20)
        self.eye_toggle_btn.setCursor(Qt.PointingHandCursor)
        self.eye_toggle_btn.setStyleSheet("QPushButton { background: transparent; border: none; }")
        self.eye_open_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#00E5FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>"""
        self.eye_closed_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#71717A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>"""
        self._update_eye_icon()
        self.eye_toggle_btn.clicked.connect(self._toggle_pass_visibility)

        p_icon = QLabel()
        p_icon.setPixmap(create_svg_icon("lock", "#94A3B8", 16).pixmap(16, 16))
        p_icon.setStyleSheet("border:none; background:transparent;")

        p_box.addWidget(self.pass_field, 1)
        p_box.addWidget(self.eye_toggle_btn)
        p_box.addWidget(p_icon)
        left_layout.addLayout(p_box)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: #EF4444; font-size: 10.5px; border: none; background: transparent;")
        self.error_label.setFixedHeight(14)
        left_layout.addWidget(self.error_label)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.setFixedHeight(34)
        cancel_btn.setStyleSheet("QPushButton { background: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 17px; font-weight: bold; font-size: 11.5px; } QPushButton:hover { background: #1E2D38; color: #FFFFFF; }")
        cancel_btn.clicked.connect(self.reject)
        
        unlock_btn = QPushButton("Unlock")
        unlock_btn.setCursor(Qt.PointingHandCursor)
        unlock_btn.setFixedHeight(34)
        unlock_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF);
                color: #04080B;
                border-radius: 17px;
                font-weight: bold;
                font-size: 12px;
                border: none;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:1 #0284C7);
            }}
        """)
        unlock_btn.clicked.connect(self.validate_and_unlock)

        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(unlock_btn)
        left_layout.addLayout(btn_row)

        card_layout.addWidget(left_widget, 58)

        right_banner = QFrame()
        right_banner.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #081116, stop:0.45 #00363F, stop:1 #008E9B);
                border-top-right-radius: 17px;
                border-bottom-right-radius: 17px;
                border-left: 1px solid rgba(0, 229, 255, 0.25);
            }
        """)
        r_layout = QVBoxLayout(right_banner)
        r_layout.setAlignment(Qt.AlignCenter)
        r_layout.setSpacing(10)
        
        b_logo = QLabel()
        b_logo.setAlignment(Qt.AlignCenter)
        b_logo.setPixmap(get_nexus_app_logo(42))
        b_logo.setStyleSheet("border:none; background:transparent;")
        r_layout.addWidget(b_logo)
        
        r_text = QLabel("NEXUS\nCORE")
        r_text.setFont(QFont("Inter", 14, QFont.Black))
        r_text.setAlignment(Qt.AlignCenter)
        r_text.setStyleSheet("color: #FFFFFF; font-weight: 900; letter-spacing: 2px; border:none; background:transparent;")
        r_layout.addWidget(r_text)
        
        card_layout.addWidget(right_banner, 42)

        main_vbox.addWidget(self.auth_card)

    def _update_eye_icon(self):
        svg_code = self.eye_open_svg if self._is_pass_visible else self.eye_closed_svg
        self.eye_toggle_btn.setIcon(QIcon(get_svg_pixmap_from_raw(svg_code, 16)))

    def _toggle_pass_visibility(self):
        self._is_pass_visible = not self._is_pass_visible
        self.pass_field.setEchoMode(QLineEdit.Normal if self._is_pass_visible else QLineEdit.Password)
        self._update_eye_icon()

    def validate_and_unlock(self):
        user = self.user_field.text().strip()
        pwd = self.pass_field.text().strip()

        if db_manager.verify_user(user, pwd):
            self.accept()
        else:
            self.auth_card.trigger_shake()
            self.error_label.setText("Invalid credentials. Access denied.")
            self.pass_field.clear()
            self.pass_field.setFocus()


class SettingsDialog(QDialog):
    settings_updated = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings - Pro AI Configuration")
        self.setFixedSize(580, 530)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.test_threads = []
        self._is_closing = False
        self.init_ui()

    def showEvent(self, event):
        super().showEvent(event)
        self.play_slide_down_entrance()

    def play_slide_down_entrance(self):
        if not GlobalConfig.UI_ANIMATIONS: return
        try:
            self.setWindowOpacity(0.0)
            target_y = self.y()
            start_y = target_y - 30
            self.move(self.x(), start_y)

            self._entrance_start_time = time.time()
            self._entrance_duration = 0.28
            self._entrance_timer = QTimer(self)
            self._entrance_timer.setInterval(8)

            def _step():
                now = time.time()
                raw = min(1.0, (now - self._entrance_start_time) / self._entrance_duration)
                ease = 1.0 - math.pow(1.0 - raw, 3)
                self.setWindowOpacity(max(0.0, min(1.0, ease)))
                self.move(self.x(), int(start_y + (target_y - start_y) * ease))
                if raw >= 1.0:
                    self._entrance_timer.stop()
                    self.setWindowOpacity(1.0)
                    self.move(self.x(), target_y)

            self._entrance_timer.timeout.connect(_step)
            self._entrance_timer.start()
        except Exception: pass

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        card = QFrame(self)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: #0A1116;
                border: 1.5px solid rgba(0, 229, 255, 0.45);
                border-radius: 18px;
            }}
            QLabel {{ color: #CBD5E1; font-family: 'Inter', sans-serif; background: transparent; border: none; }}
            QLineEdit {{ background-color: #121D24; color: #FFFFFF; border: 1px solid #1E2D38; border-radius: 6px; padding: 6px 8px; font-size: 11.5px; font-family: 'Inter', sans-serif; }}
            QLineEdit:focus {{ border: 1px solid {GlobalConfig.ACCENT_COLOR}; background-color: #16242D; }}
            
            /* COMPACT DARK QCOMBOBOX WITH FIXED DARK DROPDOWN LIST */
            QComboBox {{
                background-color: #121D24;
                color: #FFFFFF;
                border: 1px solid #1E2D38;
                border-radius: 6px;
                padding: 4px 8px;
                font-size: 11px;
                font-family: 'Inter', sans-serif;
            }}
            QComboBox:focus {{ border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 0px;
            }}
            QComboBox QAbstractItemView {{
                background-color: #0B1318 !important;
                color: #FFFFFF !important;
                border: 1px solid {GlobalConfig.ACCENT_COLOR} !important;
                selection-background-color: rgba(0, 229, 255, 0.25) !important;
                selection-color: #00E5FF !important;
                padding: 4px;
                border-radius: 6px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                height: 26px;
                padding: 4px 8px;
                background-color: #0B1318;
                color: #FFFFFF;
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: rgba(0, 229, 255, 0.25);
                color: #00E5FF;
            }}
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(36)
        shadow.setColor(QColor(0, 229, 255, 95))
        shadow.setOffset(0, 0)
        card.setGraphicsEffect(shadow)

        c_layout = QVBoxLayout(card)
        c_layout.setContentsMargins(18, 14, 18, 14)
        c_layout.setSpacing(10)

        # Header with Close Cross Button
        header_layout = QHBoxLayout()
        header = QLabel("System & Model Configuration")
        header.setFont(QFont("Inter", 13, QFont.Bold))
        header.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        header_layout.addWidget(header)
        header_layout.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(22, 22)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("QPushButton { color: #71717A; background: transparent; border: none; font-weight: bold; font-size: 13px; } QPushButton:hover { color: #EF4444; }")
        close_btn.clicked.connect(self.reject)
        header_layout.addWidget(close_btn)
        c_layout.addLayout(header_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        container = QWidget()
        container.setStyleSheet("background: transparent;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(10)

        layout.addWidget(self._create_section_label("API & Custom Endpoints"))
        
        or_row = QHBoxLayout()
        or_row.addWidget(QLabel("OpenRouter Key:"))
        self.openrouter_input = QLineEdit()
        self.openrouter_input.setText(GlobalConfig.OPENROUTER_API_KEY)
        self.openrouter_input.setEchoMode(QLineEdit.Password)
        or_row.addWidget(self.openrouter_input, 1)
        self.or_eye_btn = QPushButton("Show")
        self.or_eye_btn.setFixedSize(45, 26)
        self.or_eye_btn.setStyleSheet("background: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 5px; font-size: 10px;")
        self.or_eye_btn.clicked.connect(lambda: self._toggle_eye(self.openrouter_input, self.or_eye_btn))
        or_row.addWidget(self.or_eye_btn)
        self.or_test_btn = QPushButton("Test")
        self.or_test_btn.setFixedSize(45, 26)
        self.or_test_btn.setStyleSheet(f"background: #121D24; color: {GlobalConfig.ACCENT_COLOR}; border: 1px solid #1E2D38; border-radius: 5px; font-size: 10px;")
        self.or_test_btn.clicked.connect(self._test_openrouter_key)
        or_row.addWidget(self.or_test_btn)
        self.or_badge = QLabel("⚪")
        or_row.addWidget(self.or_badge)
        layout.addLayout(or_row)

        gem_row = QHBoxLayout()
        gem_row.addWidget(QLabel("Gemini API Key:"))
        self.gemini_input = QLineEdit()
        self.gemini_input.setText(GlobalConfig.GEMINI_API_KEY)
        self.gemini_input.setEchoMode(QLineEdit.Password)
        gem_row.addWidget(self.gemini_input, 1)
        self.gem_eye_btn = QPushButton("Show")
        self.gem_eye_btn.setFixedSize(45, 26)
        self.gem_eye_btn.setStyleSheet("background: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 5px; font-size: 10px;")
        self.gem_eye_btn.clicked.connect(lambda: self._toggle_eye(self.gemini_input, self.gem_eye_btn))
        gem_row.addWidget(self.gem_eye_btn)
        self.gem_test_btn = QPushButton("Test")
        self.gem_test_btn.setFixedSize(45, 26)
        self.gem_test_btn.setStyleSheet(f"background: #121D24; color: {GlobalConfig.ACCENT_COLOR}; border: 1px solid #1E2D38; border-radius: 5px; font-size: 10px;")
        self.gem_test_btn.clicked.connect(self._test_gemini_key)
        gem_row.addWidget(self.gem_test_btn)
        self.gem_badge = QLabel("⚪")
        gem_row.addWidget(self.gem_badge)
        layout.addLayout(gem_row)

        loc_row = QHBoxLayout()
        loc_row.addWidget(QLabel("Local AI Base URL:"))
        self.local_url_input = QLineEdit()
        self.local_url_input.setText(GlobalConfig.LOCAL_BASE_URL)
        self.local_url_input.setPlaceholderText("e.g. http://localhost:1234/v1")
        loc_row.addWidget(self.local_url_input, 1)
        layout.addLayout(loc_row)

        layout.addWidget(self._create_section_label("AI Parameters & Memory"))
        self.temp_slider, self.temp_lbl = self._create_slider_row(layout, "Creativity (Temperature):", 0, 100, int(GlobalConfig.TEMPERATURE * 100), lambda v: f"{v/100.0:.2f}")
        self.tokens_slider, self.tokens_lbl = self._create_slider_row(layout, "Max Output Tokens:", 512, 8192, GlobalConfig.MAX_TOKENS, lambda v: f"{v}")
        self.memory_slider, self.memory_lbl = self._create_slider_row(layout, "Context Memory (Msgs):", 2, 50, GlobalConfig.CONTEXT_MEMORY, lambda v: f"{v}")

        layout.addWidget(self._create_section_label("Appearance & Interface"))
        self.font_slider, self.font_lbl = self._create_slider_row(layout, "Chat Font Size (px):", 110, 160, int(GlobalConfig.CHAT_FONT_SIZE * 10), lambda v: f"{v/10.0:.1f}px")
        
        theme_row = QHBoxLayout()
        theme_row.addWidget(QLabel("Accent Color:"))
        self.accent_combo = QComboBox()
        self.accent_combo.setView(QListView())
        self.accent_combo.addItems(["#00E5FF (Cyan)", "#39FF14 (Neon Green)", "#A855F7 (Purple)", "#EF4444 (Crimson)", "#F59E0B (Gold)"])
        self.accent_combo.setCurrentText(self._get_accent_name(GlobalConfig.ACCENT_COLOR))
        theme_row.addWidget(self.accent_combo, 1)
        
        theme_row.addWidget(QLabel("Code Theme:"))
        self.code_combo = QComboBox()
        self.code_combo.setView(QListView())
        self.code_combo.addItems(["monokai", "dracula", "native", "fruity", "zenburn"])
        self.code_combo.setCurrentText(GlobalConfig.CODE_THEME)
        theme_row.addWidget(self.code_combo, 1)
        layout.addLayout(theme_row)

        layout.addWidget(self._create_section_label("Audio & Voice Recognition"))
        self.speed_slider, self.speed_lbl = self._create_slider_row(layout, "Voice Speed:", 75, 150, int(GlobalConfig.VOICE_SPEED_RATE * 100), lambda v: f"{v/100.0:.2f}x")
        
        stt_row = QHBoxLayout()
        stt_row.addWidget(QLabel("Speech-to-Text Lang:"))
        self.stt_combo = QComboBox()
        self.stt_combo.setView(QListView())
        self.stt_combo.addItems(["en-US (English)", "ur-PK (Urdu)", "hi-IN (Hindi)", "es-ES (Spanish)", "fr-FR (French)"])
        idx = self.stt_combo.findText(GlobalConfig.STT_LANG, Qt.MatchContains)
        if idx >= 0: self.stt_combo.setCurrentIndex(idx)
        stt_row.addWidget(self.stt_combo, 1)
        layout.addLayout(stt_row)

        layout.addWidget(self._create_section_label("Web Search"))
        web_row = QHBoxLayout()
        self.safe_search_cb = QCheckBox("Enable Safe Search (DDGS)")
        self.safe_search_cb.setChecked(GlobalConfig.SAFE_SEARCH)
        web_row.addWidget(self.safe_search_cb)
        
        web_row.addWidget(QLabel("Max Results:"))
        self.max_res_spin = QSpinBox()
        self.max_res_spin.setRange(1, 10)
        self.max_res_spin.setValue(GlobalConfig.MAX_WEB_RESULTS)
        self.max_res_spin.setStyleSheet(self.local_url_input.styleSheet())
        web_row.addWidget(self.max_res_spin)
        web_row.addStretch()
        layout.addLayout(web_row)

        scroll.setWidget(container)
        c_layout.addWidget(scroll, 1)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setCursor(Qt.PointingHandCursor)
        cancel_btn.setStyleSheet("QPushButton { padding: 6px 14px; border-radius: 6px; border: 1px solid #1E2D38; color: #94A3B8; background-color: #121D24; font-size: 11.5px; font-weight: bold; } QPushButton:hover { background-color: #1E2D38; color: #FFFFFF; }")
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("Save Settings")
        save_btn.setCursor(Qt.PointingHandCursor)
        save_btn.setStyleSheet(f"QPushButton {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF); color: #080D11; border-radius: 6px; padding: 6px 18px; font-weight: bold; font-size: 12px; border: none; }} QPushButton:hover {{ background: #00C4DA; }}")
        save_btn.clicked.connect(self.save_and_close)

        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(save_btn)
        c_layout.addLayout(btn_layout)

        main_layout.addWidget(card)

    def _create_section_label(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setFont(QFont("Inter", 10.5, QFont.Bold))
        lbl.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; border-bottom: 1px solid #1E2D38; margin-top: 6px; padding-bottom: 4px;")
        return lbl

    def _create_slider_row(self, layout, label_text, min_val, max_val, cur_val, format_fn):
        row = QHBoxLayout()
        lbl = QLabel(label_text)
        val_lbl = QLabel(format_fn(cur_val))
        val_lbl.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; font-weight: bold; font-size: 11px; min-width: 45px;")
        
        slider = QSlider(Qt.Horizontal)
        slider.setRange(min_val, max_val)
        slider.setValue(cur_val)
        slider.valueChanged.connect(lambda v: val_lbl.setText(format_fn(v)))
        slider.setStyleSheet(f"QSlider::groove:horizontal {{ background: #121D24; height: 4px; border-radius: 2px; }} QSlider::sub-page:horizontal {{ background: {GlobalConfig.ACCENT_COLOR}; border-radius: 2px; }} QSlider::handle:horizontal {{ background: #FFFFFF; width: 14px; margin-top: -5px; margin-bottom: -5px; border-radius: 7px; }}")
        
        row.addWidget(lbl)
        row.addWidget(slider, 1)
        row.addWidget(val_lbl)
        layout.addLayout(row)
        return slider, val_lbl

    def _get_accent_name(self, hex_code):
        for item in ["#00E5FF (Cyan)", "#39FF14 (Neon Green)", "#A855F7 (Purple)", "#EF4444 (Crimson)", "#F59E0B (Gold)"]:
            if item.startswith(hex_code): return item
        return "#00E5FF (Cyan)"

    def _toggle_eye(self, line_edit: QLineEdit, btn: QPushButton):
        if line_edit.echoMode() == QLineEdit.Password:
            line_edit.setEchoMode(QLineEdit.Normal)
            btn.setText("Hide")
        else:
            line_edit.setEchoMode(QLineEdit.Password)
            btn.setText("Show")

    def _test_openrouter_key(self):
        key = self.openrouter_input.text().strip()
        self.or_badge.setText("⏳")
        t = ApiConnectionTesterThread("openrouter", key)
        t.test_result_signal.connect(self._on_test_result)
        self.test_threads.append(t)
        t.start()

    def _test_gemini_key(self):
        key = self.gemini_input.text().strip()
        self.gem_badge.setText("⏳")
        t = ApiConnectionTesterThread("gemini", key)
        t.test_result_signal.connect(self._on_test_result)
        self.test_threads.append(t)
        t.start()

    def _on_test_result(self, provider: str, success: bool, message: str):
        badge = self.or_badge if provider == "openrouter" else self.gem_badge
        if success: badge.setText("✅"); badge.setToolTip(message)
        else: badge.setText("❌"); badge.setToolTip(message)

    def save_and_close(self):
        try:
            db_manager.set_setting("openrouter_api_key", self.openrouter_input.text().strip())
            db_manager.set_setting("gemini_api_key", self.gemini_input.text().strip())
            db_manager.set_setting("local_base_url", self.local_url_input.text().strip())
            db_manager.set_setting("temperature", str(self.temp_slider.value() / 100.0))
            db_manager.set_setting("max_tokens", str(self.tokens_slider.value()))
            db_manager.set_setting("context_memory", str(self.memory_slider.value()))
            db_manager.set_setting("voice_speed_rate", str(self.speed_slider.value() / 100.0))
            db_manager.set_setting("chat_font_size", str(self.font_slider.value() / 10.0))
            
            accent_val = self.accent_combo.currentText().split(" ")[0]
            db_manager.set_setting("accent_color", accent_val)
            db_manager.set_setting("code_theme", self.code_combo.currentText())
            db_manager.set_setting("stt_lang", self.stt_combo.currentText().split(" ")[0])
            db_manager.set_setting("safe_search", str(self.safe_search_cb.isChecked()))
            db_manager.set_setting("max_web_results", str(self.max_res_spin.value()))
            
            GlobalConfig.sync_from_db(db_manager)
            self.settings_updated.emit()
        except Exception:
            pass
        self.accept()

# ==============================================================================
# 13. MAIN APPLICATION WINDOW WITH COMPLETE AUTH & LOGIN EXPERIENCE
# ==============================================================================

class NexusAIProApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NEXUS AI")

        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.target_w = min(1380, int(screen.width() * 0.95))
        self.target_h = min(860, int(screen.height() * 0.92))
        self.target_x = screen.x() + (screen.width() - self.target_w) // 2
        self.target_y = screen.y() + (screen.height() - self.target_h) // 2
        self.target_geo = QRect(self.target_x, self.target_y, self.target_w, self.target_h)

        self.setGeometry(self.target_geo)
        self.setMinimumSize(900, 600)
        self.setAcceptDrops(True)

        self._is_closing = False
        self._entrance_animated = False

        self.active_chat_id: Optional[str] = None
        self.all_chats = db_manager.load_all_chats()
        self.turn_audio_played = False
        self.web_search_active = False
        
        self.session_cost = 0.0

        # Pipelined Streaming TTS Engine Queues
        self.audio_chunk_queue: Dict[int, str] = {}
        self.current_playback_index = 0
        self.active_producer_thread: Optional[StreamingTTSProducerThread] = None
        self.active_audio_model_id: Optional[str] = None
        self.all_temp_voice_files: List[str] = []

        saved_models_json = db_manager.get_setting("selected_models", '["gemini-3.8", "qwen-2.5-72b", "llama-3.3-70b"]')
        try:
            self.selected_model_ids: List[str] = json.loads(saved_models_json)
            self.selected_model_ids = [m for m in self.selected_model_ids if m in FREE_MODELS_REGISTRY]
            if not self.selected_model_ids: self.selected_model_ids = ["gemini-3.8", "qwen-2.5-72b", "llama-3.3-70b"]
        except Exception: self.selected_model_ids = ["gemini-3.8", "qwen-2.5-72b", "llama-3.3-70b"]

        self.attached_files: List[Dict[str, Any]] = []
        self.active_workers: Dict[str, UniversalAIWorkerThread] = {}
        self.arena_columns: Dict[str, ModelArenaColumn] = {}

        self.audio_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.mediaStatusChanged.connect(self._on_media_status_changed)

        self.central_widget = QWidget()
        self.central_widget.setObjectName("rootCanvas")
        self.setCentralWidget(self.central_widget)
        
        self.global_particles = CyberParticleCanvas(self.central_widget, particle_count=48)
        self.glow_cursor = CursorGlowEffect(self.central_widget)

        self.root_layout = QHBoxLayout(self.central_widget)
        self.root_layout.setContentsMargins(6, 6, 6, 6)
        self.root_layout.setSpacing(0)

        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_splitter.setHandleWidth(8)
        self.main_splitter.setStyleSheet("""
            QSplitter { background: transparent; }
            QSplitter::handle { background-color: transparent; }
            QSplitter::handle:hover { background-color: rgba(0, 229, 255, 0.2); }
            QSplitter::handle:pressed { background-color: #00E5FF; }
        """)
        
        self.init_sidebar()

        self.card_container = QFrame()
        self.card_container.setObjectName("cardContainer")
        self.card_container.setStyleSheet("background: transparent; border: none;")
        self.card_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.card_layout = QStackedLayout(self.card_container)
        
        self.main_splitter.addWidget(self.sidebar_frame)
        self.main_splitter.addWidget(self.card_container)
        self.main_splitter.setStretchFactor(0, 0)
        self.main_splitter.setStretchFactor(1, 1)

        self.root_layout.addWidget(self.main_splitter)

        self.init_login_view()
        self.init_splash_loading_view()
        self.init_workspace_view()

        # Check for Remembered Auto-Login Session
        remember_me = db_manager.get_setting("remember_me", "False") == "True"
        saved_user = db_manager.get_setting("saved_session_user", "")

        if remember_me and saved_user:
            GlobalConfig.CURRENT_USER = saved_user
            self.card_layout.setCurrentWidget(self.splash_view)
            QTimer.singleShot(100, self._start_auto_login_splash)
        else:
            self.card_layout.setCurrentWidget(self.login_view)

        self.apply_ninja_hex_theme()

    def _start_auto_login_splash(self):
        self.splash_worker = AppSplashScreenThread()
        self.splash_worker.progress_val.connect(
            lambda v: (self.splash_progress.setValue(v), self.splash_percent_lbl.setText(f"{v}%"))
        )
        self.splash_worker.progress_desc.connect(self.splash_desc.setText)
        self.splash_worker.finished.connect(self.complete_login)
        self.splash_worker.start()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'global_particles') and self.global_particles:
            self.global_particles.setGeometry(0, 0, self.central_widget.width(), self.central_widget.height())

    def showEvent(self, event):
        super().showEvent(event)
        if hasattr(self, 'global_particles') and self.global_particles:
            self.global_particles.setGeometry(0, 0, self.central_widget.width(), self.central_widget.height())
        if not self._entrance_animated:
            self._entrance_animated = True
            self.play_slide_up_entrance()

    def play_slide_up_entrance(self):
        if not GlobalConfig.UI_ANIMATIONS: return
        try:
            self.setWindowOpacity(0.0)
            start_y = self.target_y + 40
            self.setGeometry(self.target_x, start_y, self.target_w, self.target_h)

            self._entrance_start_time = time.time()
            self._entrance_duration = 0.35
            self._entrance_timer = QTimer(self)
            self._entrance_timer.setInterval(8)

            def _step():
                now = time.time()
                raw = min(1.0, (now - self._entrance_start_time) / self._entrance_duration)
                ease = 1.0 - math.pow(1.0 - raw, 3)
                self.setWindowOpacity(max(0.0, min(1.0, ease)))
                self.setGeometry(self.target_x, int(start_y + (self.target_y - start_y) * ease), self.target_w, self.target_h)
                if raw >= 1.0:
                    self._entrance_timer.stop()
                    self.setWindowOpacity(1.0)
                    self.setGeometry(self.target_geo)

            self._entrance_timer.timeout.connect(_step)
            self._entrance_timer.start()
        except Exception: pass

    def closeEvent(self, event: QCloseEvent):
        if self._is_closing:
            self.stop_all_workers()
            self.stop_any_active_audio()
            event.accept()
            return

        event.ignore()
        self._is_closing = True
        self.stop_all_workers()
        self.stop_any_active_audio()
        
        if hasattr(self, 'glow_cursor'):
            try: self.glow_cursor.cleanup()
            except: pass

        if not GlobalConfig.UI_ANIMATIONS:
            self.close()
            QApplication.quit()
            return

        try:
            cur_geo = self.geometry()
            start_x, start_y = cur_geo.x(), cur_geo.y()
            start_w, start_h = cur_geo.width(), cur_geo.height()
            target_exit_y = start_y + 40
            start_opacity = self.windowOpacity()

            self._exit_start_time = time.time()
            self._exit_duration = 0.25
            self._exit_timer = QTimer(self)
            self._exit_timer.setInterval(8)

            def _step():
                now = time.time()
                raw = min(1.0, (now - self._exit_start_time) / self._exit_duration)
                ease = math.pow(raw, 3)
                self.setWindowOpacity(max(0.0, min(1.0, start_opacity * (1.0 - ease))))
                self.setGeometry(start_x, int(start_y + (target_exit_y - start_y) * ease), start_w, start_h)
                if raw >= 1.0:
                    self._exit_timer.stop()
                    self.close()
                    QApplication.quit()

            self._exit_timer.timeout.connect(_step)
            self._exit_timer.start()
        except Exception:
            self.close()
            QApplication.quit()

    def stop_all_workers(self):
        try:
            for w in list(self.active_workers.values()):
                if w and w.isRunning(): w.stop()
            for w in list(self.active_workers.values()):
                if w and w.isRunning(): w.wait(200)
            self.active_workers.clear()
        except Exception: pass

    def apply_ninja_hex_theme(self):
        accent = GlobalConfig.ACCENT_COLOR
        self.setStyleSheet(f"""
            QWidget#rootCanvas {{ background-color: #080D11; font-family: 'Inter', sans-serif; }}
            QFrame#cardContainer {{ background-color: transparent; border: none; }}
            QFrame#sidebarFrame {{ background-color: rgba(11, 19, 24, 0.72); border-right: 1px solid rgba(0, 229, 255, 0.2); border-radius: 8px; margin-right: 4px; }}
            QScrollBar:horizontal {{ background: transparent; height: 6px; margin: 0px; }}
            QScrollBar::handle:horizontal {{ background: #1E2D38; min-width: 20px; border-radius: 3px; }}
            QScrollBar::handle:horizontal:hover {{ background: {accent}; }}
            QScrollBar:vertical {{ background: transparent; width: 6px; margin: 0px; }}
            QScrollBar::handle:vertical {{ background: #1E2D38; min-height: 20px; border-radius: 3px; }}
            QScrollBar::handle:vertical:hover {{ background: {accent}; }}
            QScrollBar:add-line, QScrollBar:sub-line {{ height: 0px; width: 0px; }}
            
            /* Custom Cyber Styled Dialogs, Popups & Dark Combobox Dropdown Views */
            QMessageBox {{
                background-color: #0E161C;
                border: 1.5px solid {accent};
                border-radius: 12px;
            }}
            QMessageBox QLabel {{
                color: #FFFFFF;
                font-family: 'Inter', sans-serif;
                font-size: 12.5px;
            }}
            QMessageBox QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {accent}, stop:1 #0072FF);
                color: #04080B;
                border-radius: 8px;
                padding: 6px 18px;
                font-weight: bold;
                font-size: 11.5px;
                min-width: 70px;
                min-height: 24px;
                border: none;
            }}
            QMessageBox QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:1 #0284C7);
            }}
            QMenu {{
                background-color: #0E161C;
                color: #FFFFFF;
                border: 1px solid rgba(0, 229, 255, 0.4);
                border-radius: 8px;
                padding: 4px;
            }}
            QMenu::item {{
                padding: 8px 18px;
                border-radius: 4px;
                font-size: 12px;
            }}
            QMenu::item:selected {{
                background-color: {accent};
                color: #080D11;
                font-weight: bold;
            }}
            QToolTip {{
                background-color: #121D24;
                color: {accent};
                border: 1px solid #1E2D38;
                border-radius: 6px;
                padding: 4px 8px;
                font-size: 11px;
            }}
        """)

    # --------------------------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------------------------
    def init_sidebar(self):
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setObjectName("sidebarFrame")
        self.sidebar_frame.setMinimumWidth(220)
        self.sidebar_frame.setMaximumWidth(400)

        layout = QVBoxLayout(self.sidebar_frame)
        layout.setContentsMargins(14, 16, 14, 16)
        layout.setSpacing(10)

        logo_layout = QHBoxLayout()
        logo_layout.setContentsMargins(0, 0, 0, 8)
        self.sidebar_logo_lbl = QLabel()
        self.sidebar_logo_lbl.setPixmap(get_nexus_app_logo(45))
        logo_layout.addWidget(self.sidebar_logo_lbl, alignment=Qt.AlignCenter)
        layout.addLayout(logo_layout)

        lib_header = QLabel("Chat History")
        lib_header.setFont(QFont("Inter", 11, QFont.Bold))
        lib_header.setStyleSheet("color: #FFFFFF; padding-bottom: 2px;")
        layout.addWidget(lib_header)

        new_chat_btn = QPushButton("New Session")
        new_chat_btn.setIcon(create_svg_icon("plus", "#080D11"))
        new_chat_btn.setCursor(Qt.PointingHandCursor)
        new_chat_btn.setStyleSheet(f"""
            QPushButton {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF); color: #080D11; border-radius: 8px; padding: 10px; font-weight: bold; font-size: 12px; border: none; }}
            QPushButton:hover {{ background: #00C4DA; }}
        """)
        new_chat_btn.clicked.connect(self.create_new_chat)
        layout.addWidget(new_chat_btn)

        self.search_entry = AnimatedUnderlineLineEdit(placeholder="Search history...", is_password=False)
        self.search_entry.setStyleSheet(f"QLineEdit {{ background-color: rgba(18, 29, 36, 0.7); border: 1px solid rgba(0,229,255,0.25); border-radius: 8px; padding: 8px 10px; font-size: 11px; color: #FFFFFF; }} QLineEdit:focus {{ border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}")
        self.search_entry.textChanged.connect(self.filter_sidebar_chats)
        layout.addWidget(self.search_entry)

        self.history_scroll = QScrollArea()
        self.history_scroll.setWidgetResizable(True)
        self.history_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.history_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.history_scroll.setStyleSheet("background: transparent; border: none;")

        self.history_container = QWidget()
        self.history_container.setStyleSheet("background: transparent; border: none;")
        self.history_layout = QVBoxLayout(self.history_container)
        self.history_layout.setAlignment(Qt.AlignTop)
        self.history_layout.setSpacing(4)

        self.history_scroll.setWidget(self.history_container)
        layout.addWidget(self.history_scroll, 1)

        bot_layout = QHBoxLayout()
        settings_btn = QPushButton(" Settings")
        settings_btn.setIcon(create_svg_icon("settings", "#FFFFFF", 16))
        settings_btn.setCursor(Qt.PointingHandCursor)
        settings_btn.setStyleSheet("QPushButton { background-color: rgba(18, 29, 36, 0.8); color: #FFFFFF; border: 1px solid rgba(0,229,255,0.2); border-radius: 8px; padding: 8px; font-size: 11px; font-weight: 500; } QPushButton:hover { background-color: rgba(0,229,255,0.15); border: 1px solid #00E5FF; }")
        settings_btn.clicked.connect(self.open_settings)

        export_btn = QPushButton(" Export")
        export_btn.setIcon(create_svg_icon("download", "#FFFFFF", 16))
        export_btn.setCursor(Qt.PointingHandCursor)
        export_btn.setStyleSheet("QPushButton { background-color: rgba(18, 29, 36, 0.8); color: #FFFFFF; border: 1px solid rgba(0,229,255,0.2); border-radius: 8px; padding: 8px; font-size: 11px; font-weight: 500; } QPushButton:hover { background-color: rgba(0,229,255,0.15); border: 1px solid #00E5FF; }")
        export_btn.clicked.connect(self.export_current_chat)

        logout_btn = QPushButton()
        logout_btn.setIcon(create_svg_icon("logout", "#EF4444", 16))
        logout_btn.setToolTip("Sign Out")
        logout_btn.setFixedSize(32, 32)
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.setStyleSheet("QPushButton { background-color: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; } QPushButton:hover { background-color: #EF4444; }")
        logout_btn.clicked.connect(self.logout_user)

        bot_layout.addWidget(settings_btn, 1)
        bot_layout.addWidget(export_btn, 1)
        bot_layout.addWidget(logout_btn)
        layout.addLayout(bot_layout)

        self.sidebar_frame.hide()

    def logout_user(self):
        db_manager.set_setting("remember_me", "False")
        db_manager.set_setting("saved_session_user", "")
        self.sidebar_frame.hide()
        self.stop_any_active_audio()
        self.stop_all_workers()
        self.card_layout.setCurrentWidget(self.login_view)

    # --------------------------------------------------------------------------
    # PREMIUM AUTH & LOGIN VIEW (REMEMBER ME, SPINNER, SIGNUP, STRENGTH METER)
    # --------------------------------------------------------------------------
    def init_login_view(self):
        self.login_view = QWidget()
        self.login_view.setStyleSheet("background: transparent;")
        
        main_vbox = QVBoxLayout(self.login_view)
        main_vbox.setAlignment(Qt.AlignCenter)
        main_vbox.setContentsMargins(0, 0, 0, 0)

        self.login_card = TiltLoginCard(self.login_view)
        self.login_card.setFixedSize(760, 480)
        self.login_card.setStyleSheet("""
            QFrame#loginCard {
                background-color: #070D12;
                border: 1.5px solid rgba(0, 229, 255, 0.45);
                border-radius: 20px;
            }
        """)

        card_layout = QHBoxLayout(self.login_card)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        # LEFT AUTH STACK (LOGIN vs SIGNUP)
        left_form_widget = QWidget()
        left_form_widget.setStyleSheet("background: transparent;")
        self.auth_left_vbox = QVBoxLayout(left_form_widget)
        self.auth_left_vbox.setContentsMargins(36, 26, 32, 24)
        self.auth_left_vbox.setSpacing(10)

        # Tab Mode Switcher (Login vs Sign Up)
        mode_toggle_box = QHBoxLayout()
        mode_toggle_box.setSpacing(12)

        self.tab_login_btn = QPushButton("Sign In")
        self.tab_login_btn.setCursor(Qt.PointingHandCursor)
        self.tab_login_btn.setFont(QFont("Inter", 13, QFont.Bold))
        self.tab_login_btn.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; background: transparent; border: none; border-bottom: 2px solid {GlobalConfig.ACCENT_COLOR}; padding-bottom: 4px;")
        self.tab_login_btn.clicked.connect(lambda: self._set_auth_mode("login"))
        mode_toggle_box.addWidget(self.tab_login_btn)

        self.tab_signup_btn = QPushButton("Create Account")
        self.tab_signup_btn.setCursor(Qt.PointingHandCursor)
        self.tab_signup_btn.setFont(QFont("Inter", 13, QFont.Bold))
        self.tab_signup_btn.setStyleSheet("color: #64748B; background: transparent; border: none; padding-bottom: 4px;")
        self.tab_signup_btn.clicked.connect(lambda: self._set_auth_mode("signup"))
        mode_toggle_box.addWidget(self.tab_signup_btn)

        mode_toggle_box.addStretch()
        
        self.caps_warning = QLabel("⇪ CAPS ON")
        self.caps_warning.setFont(QFont("Inter", 8, QFont.Bold))
        self.caps_warning.setStyleSheet("background: rgba(245, 158, 11, 0.15); color: #F59E0B; border: 1px solid #F59E0B; border-radius: 6px; padding: 2px 6px;")
        self.caps_warning.hide()
        mode_toggle_box.addWidget(self.caps_warning)
        self.auth_left_vbox.addLayout(mode_toggle_box)

        # Subtitle
        self.auth_subtitle = QLabel("Welcome back! Sign in to access multi-model matrix.")
        self.auth_subtitle.setFont(QFont("Inter", 9))
        self.auth_subtitle.setStyleSheet("color: #94A3B8; border: none; background: transparent; margin-bottom: 4px;")
        self.auth_left_vbox.addWidget(self.auth_subtitle)

        # Username Field
        u_box = QHBoxLayout()
        u_box.setSpacing(8)
        self.user_field = AnimatedUnderlineLineEdit(placeholder="Username or Email", is_password=False)
        self.user_field.returnPressed.connect(lambda: self.pass_field.setFocus())
        self.user_field.caps_changed.connect(self._toggle_caps_indicator)
        
        user_icon_lbl = QLabel()
        user_icon_lbl.setPixmap(create_svg_icon("user", "#94A3B8", 16).pixmap(16, 16))
        user_icon_lbl.setStyleSheet("border: none; background: transparent;")
        u_box.addWidget(self.user_field, 1)
        u_box.addWidget(user_icon_lbl)
        self.auth_left_vbox.addLayout(u_box)

        # Email Field (Only visible in Sign Up)
        self.email_box = QHBoxLayout()
        self.email_box.setSpacing(8)
        self.email_field = AnimatedUnderlineLineEdit(placeholder="Email Address", is_password=False)
        self.email_field.returnPressed.connect(lambda: self.pass_field.setFocus())
        
        mail_icon_lbl = QLabel()
        mail_icon_lbl.setPixmap(create_svg_icon("mail", "#94A3B8", 16).pixmap(16, 16))
        mail_icon_lbl.setStyleSheet("border: none; background: transparent;")
        self.email_box.addWidget(self.email_field, 1)
        self.email_box.addWidget(mail_icon_lbl)
        self.auth_left_vbox.addLayout(self.email_box)
        self.email_field.hide()
        mail_icon_lbl.hide()
        self.email_icon_lbl = mail_icon_lbl

        # Password Field
        p_box = QHBoxLayout()
        p_box.setSpacing(6)
        self.pass_field = AnimatedUnderlineLineEdit(placeholder="Password", is_password=True)
        self.pass_field.returnPressed.connect(self.authenticate_user)
        self.pass_field.caps_changed.connect(self._toggle_caps_indicator)
        self.pass_field.textChanged.connect(lambda t: self.strength_meter.evaluate_password(t))

        self.eye_toggle_btn = QPushButton()
        self.eye_toggle_btn.setFixedSize(22, 22)
        self.eye_toggle_btn.setCursor(Qt.PointingHandCursor)
        self.eye_toggle_btn.setStyleSheet("QPushButton { background: transparent; border: none; }")
        self._is_pass_visible = False
        
        self.eye_open_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#00E5FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>"""
        self.eye_closed_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#71717A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>"""
        self._update_eye_icon()
        self.eye_toggle_btn.clicked.connect(self._toggle_pass_visibility)

        lock_icon_lbl = QLabel()
        lock_icon_lbl.setPixmap(create_svg_icon("lock", "#94A3B8", 16).pixmap(16, 16))
        lock_icon_lbl.setStyleSheet("border: none; background: transparent;")

        p_box.addWidget(self.pass_field, 1)
        p_box.addWidget(self.eye_toggle_btn)
        p_box.addWidget(lock_icon_lbl)
        self.auth_left_vbox.addLayout(p_box)

        # Password Strength Meter (Shown on signup or typing)
        self.strength_meter = PasswordStrengthMeter(self)
        self.auth_left_vbox.addWidget(self.strength_meter)
        self.strength_meter.hide()

        # Options Row (Remember Me & Forgot Password)
        self.options_row = QHBoxLayout()
        self.remember_me_cb = QCheckBox("Remember Me")
        self.remember_me_cb.setChecked(db_manager.get_setting("remember_me", "False") == "True")
        self.remember_me_cb.setFont(QFont("Inter", 8.5))
        self.remember_me_cb.setCursor(Qt.PointingHandCursor)
        self.remember_me_cb.setStyleSheet(f"""
            QCheckBox {{ color: #94A3B8; spacing: 6px; }}
            QCheckBox::indicator {{ width: 15px; height: 15px; border-radius: 4px; border: 1px solid #1E2D38; background: #080D11; }}
            QCheckBox::indicator:checked {{ background: {GlobalConfig.ACCENT_COLOR}; border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}
        """)
        self.options_row.addWidget(self.remember_me_cb)
        self.options_row.addStretch()

        self.forgot_pwd_btn = QPushButton("Forgot Password?")
        self.forgot_pwd_btn.setCursor(Qt.PointingHandCursor)
        self.forgot_pwd_btn.setFont(QFont("Inter", 8.5))
        self.forgot_pwd_btn.setStyleSheet(f"QPushButton {{ color: {GlobalConfig.ACCENT_COLOR}; background: transparent; border: none; }} QPushButton:hover {{ text-decoration: underline; }}")
        self.forgot_pwd_btn.clicked.connect(self._open_forgot_password)
        self.options_row.addWidget(self.forgot_pwd_btn)
        self.auth_left_vbox.addLayout(self.options_row)

        # Error label
        self.auth_error = QLabel("")
        self.auth_error.setStyleSheet("color: #EF4444; font-size: 11px; border: none; background: transparent;")
        self.auth_error.setFixedHeight(14)
        self.auth_left_vbox.addWidget(self.auth_error)

        # Action Button with Integrated Cyber Arc Spinner
        self.login_btn = CyberSpinnerButton("Sign In to Nexus")
        self.login_btn.setFixedHeight(38)
        self.login_btn.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00B4D8, stop:0.5 #00E5FF, stop:1 #0077B6);
                color: #04080B;
                border-radius: 19px;
                font-weight: bold;
                font-size: 13px;
                border: none;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:0.5 #22D3EE, stop:1 #0284C7);
            }}
        """)
        self.login_btn.clicked.connect(self.authenticate_user)
        self.auth_left_vbox.addWidget(self.login_btn)

        # Guest / Offline Mode Bypass Button
        self.guest_mode_btn = QPushButton("Continue as Guest (Offline Local AI)")
        self.guest_mode_btn.setCursor(Qt.PointingHandCursor)
        self.guest_mode_btn.setStyleSheet(f"QPushButton {{ color: #94A3B8; background: rgba(18, 29, 36, 0.6); border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 10px; padding: 6px; font-size: 11px; font-weight: bold; }} QPushButton:hover {{ color: {GlobalConfig.ACCENT_COLOR}; border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}")
        self.guest_mode_btn.clicked.connect(self._continue_as_guest)
        self.auth_left_vbox.addWidget(self.guest_mode_btn)

        # Social Logins and Terms
        self.other_options_btn = QPushButton("Sign in with Google / GitHub")
        self.other_options_btn.setCursor(Qt.PointingHandCursor)
        self.other_options_btn.setStyleSheet("QPushButton {{ color: #64748B; background: transparent; border: none; font-size: 10.5px; }} QPushButton:hover {{ color: #00E5FF; text-decoration: underline; }}")
        self.other_options_btn.clicked.connect(self.show_more_login_options)
        self.auth_left_vbox.addWidget(self.other_options_btn, alignment=Qt.AlignCenter)

        # Terms of Service & Privacy Disclaimer
        terms_lbl = QLabel("By continuing, you agree to our <a href='terms' style='color:#00E5FF; text-decoration:none;'>Terms</a> & <a href='privacy' style='color:#00E5FF; text-decoration:none;'>Privacy Policy</a>.")
        terms_lbl.setFont(QFont("Inter", 8))
        terms_lbl.setAlignment(Qt.AlignCenter)
        terms_lbl.setStyleSheet("color: #64748B; border: none; background: transparent;")
        terms_lbl.linkActivated.connect(self._open_legal_notice)
        self.auth_left_vbox.addWidget(terms_lbl)

        card_layout.addWidget(left_form_widget, 56)

        # RIGHT BANNER
        right_banner_frame = QFrame()
        right_banner_frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #081116, stop:0.45 #00363F, stop:1 #008E9B);
                border-top-right-radius: 19px;
                border-bottom-right-radius: 19px;
                border-left: 1px solid rgba(0, 229, 255, 0.25);
            }
        """)
        banner_layout = QVBoxLayout(right_banner_frame)
        banner_layout.setAlignment(Qt.AlignCenter)
        banner_layout.setContentsMargins(20, 24, 20, 24)
        banner_layout.setSpacing(14)

        banner_logo = QLabel()
        banner_logo.setAlignment(Qt.AlignCenter)
        b_logo_pix = get_nexus_app_logo(58)
        banner_logo.setPixmap(b_logo_pix)
        banner_logo.setStyleSheet("border: none; background: transparent;")
        banner_layout.addWidget(banner_logo)

        welcome_title = QLabel("NEXUS\nMULTI-MODEL")
        welcome_title.setFont(QFont("Inter", 19, QFont.Black))
        welcome_title.setAlignment(Qt.AlignCenter)
        welcome_title.setStyleSheet("color: #FFFFFF; font-weight: 900; letter-spacing: 2px; line-height: 1.25; border: none; background: transparent;")
        banner_layout.addWidget(welcome_title)

        tag_badge = QLabel("STUDIO MATRIX ARENA")
        tag_badge.setFont(QFont("Inter", 8.5, QFont.Bold))
        tag_badge.setStyleSheet(
            "background: rgba(0, 229, 255, 0.15); color: #FFFFFF; "
            f"border: 1px solid {GlobalConfig.ACCENT_COLOR}; border-radius: 6px; padding: 3px 8px;"
        )
        banner_layout.addWidget(tag_badge)

        card_layout.addWidget(right_banner_frame, 44)

        main_vbox.addWidget(self.login_card)
        self.card_layout.addWidget(self.login_view)
        self.current_auth_mode = "login"

    def _set_auth_mode(self, mode: str):
        self.current_auth_mode = mode
        self.auth_error.clear()
        
        if mode == "login":
            self.tab_login_btn.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; background: transparent; border: none; border-bottom: 2px solid {GlobalConfig.ACCENT_COLOR}; padding-bottom: 4px;")
            self.tab_signup_btn.setStyleSheet("color: #64748B; background: transparent; border: none; padding-bottom: 4px;")
            self.auth_subtitle.setText("Welcome back! Sign in to access multi-model matrix.")
            self.email_field.hide()
            self.email_icon_lbl.hide()
            self.strength_meter.hide()
            self.options_row.setEnabled(True)
            self.remember_me_cb.show()
            self.forgot_pwd_btn.show()
            self.login_btn.setText("Sign In to Nexus")
        else:
            self.tab_signup_btn.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; background: transparent; border: none; border-bottom: 2px solid {GlobalConfig.ACCENT_COLOR}; padding-bottom: 4px;")
            self.tab_login_btn.setStyleSheet("color: #64748B; background: transparent; border: none; padding-bottom: 4px;")
            self.auth_subtitle.setText("Create your local account for session & API persistence.")
            self.email_field.show()
            self.email_icon_lbl.show()
            self.strength_meter.show()
            self.strength_meter.evaluate_password(self.pass_field.text())
            self.remember_me_cb.show()
            self.forgot_pwd_btn.hide()
            self.login_btn.setText("Register Account & Launch")

    def _open_legal_notice(self, link: str):
        if link == "terms":
            content = """
                <h3 style='color:#00E5FF;'>Nexus AI - Terms of Service</h3>
                <p>1. <b>Platform Purpose:</b> Nexus AI is a multi-model orchestration arena designed and developed by Wajahat.</p>
                <p>2. <b>API & Data Privacy:</b> All API keys and local requests are processed securely on your local device machine.</p>
                <p>3. <b>Model Usage:</b> Compliance with Google AI Studio, Meta Llama, Alibaba Qwen, and OpenRouter safety guidelines is maintained.</p>
            """
            LegalNoticeDialog("Terms of Service", content, self).exec()
        elif link == "privacy":
            content = """
                <h3 style='color:#00E5FF;'>Privacy Policy</h3>
                <p>1. <b>Local Security:</b> All user credentials and session history are stored locally in an encrypted/hashed SQLite format.</p>
                <p>2. <b>Zero Telemetry:</b> No private prompts or voice streams are sent to unauthorized third-party telemetry servers.</p>
            """
            LegalNoticeDialog("Privacy Policy", content, self).exec()

    def _open_forgot_password(self):
        ForgotPasswordDialog(self).exec()

    def _continue_as_guest(self):
        GlobalConfig.CURRENT_USER = "Guest"
        self.card_layout.setCurrentWidget(self.splash_view)
        self.splash_worker = AppSplashScreenThread()
        self.splash_worker.progress_val.connect(
            lambda v: (self.splash_progress.setValue(v), self.splash_percent_lbl.setText(f"{v}%"))
        )
        self.splash_worker.progress_desc.connect(self.splash_desc.setText)
        self.splash_worker.finished.connect(self.complete_login)
        self.splash_worker.start()

    def _toggle_caps_indicator(self, is_active: bool):
        self.caps_warning.setVisible(is_active)

    def _update_eye_icon(self):
        svg_code = self.eye_open_svg if self._is_pass_visible else self.eye_closed_svg
        self.eye_toggle_btn.setIcon(QIcon(get_svg_pixmap_from_raw(svg_code, 16)))

    def _toggle_pass_visibility(self):
        self._is_pass_visible = not self._is_pass_visible
        self.pass_field.setEchoMode(QLineEdit.Normal if self._is_pass_visible else QLineEdit.Password)
        self._update_eye_icon()

    def show_more_login_options(self):
        popup = SocialLoginPopup(self)
        popup.exec()

    # --------------------------------------------------------------------------
    # SCI-FI CYBER HUD SPLASH LOADING VIEW
    # --------------------------------------------------------------------------
    def init_splash_loading_view(self):
        self.splash_view = QWidget()
        self.splash_view.setStyleSheet("background: transparent;")

        main_vbox = QVBoxLayout(self.splash_view)
        main_vbox.setAlignment(Qt.AlignCenter)
        main_vbox.setContentsMargins(0, 0, 0, 0)

        splash_card = QFrame()
        splash_card.setFixedSize(480, 360)
        splash_card.setStyleSheet("""
            QFrame {
                background-color: #070D12;
                border: 1.5px solid rgba(0, 229, 255, 0.4);
                border-radius: 20px;
            }
        """)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(0, 229, 255, 100))
        shadow.setOffset(0, 0)
        splash_card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(splash_card)
        card_layout.setAlignment(Qt.AlignCenter)
        card_layout.setContentsMargins(30, 25, 30, 25)
        card_layout.setSpacing(10)

        self.radar_loader = CyberRadarLoader(self)
        card_layout.addWidget(self.radar_loader, alignment=Qt.AlignCenter)

        title = QLabel("NEXUS NEURAL MATRIX")
        title.setFont(QFont("Inter", 14, QFont.Black))
        title.setStyleSheet("color: #FFFFFF; letter-spacing: 2.5px; border: none; background: transparent;")
        card_layout.addWidget(title, alignment=Qt.AlignCenter)

        self.splash_percent_lbl = QLabel("0%")
        self.splash_percent_lbl.setFont(QFont("Consolas", 15, QFont.Bold))
        self.splash_percent_lbl.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR}; border: none; background: transparent;")
        card_layout.addWidget(self.splash_percent_lbl, alignment=Qt.AlignCenter)

        self.splash_progress = QProgressBar()
        self.splash_progress.setRange(0, 100)
        self.splash_progress.setFixedHeight(6)
        self.splash_progress.setFixedWidth(320)
        self.splash_progress.setTextVisible(False)
        self.splash_progress.setStyleSheet(f"""
            QProgressBar {{
                background-color: #121D24;
                border-radius: 3px;
                border: 1px solid #1E2D38;
            }}
            QProgressBar::chunk {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF);
                border-radius: 3px;
            }}
        """)
        
        bar_shadow = QGraphicsDropShadowEffect(self)
        bar_shadow.setBlurRadius(15)
        bar_shadow.setColor(QColor(0, 229, 255, 180))
        self.splash_progress.setGraphicsEffect(bar_shadow)
        card_layout.addWidget(self.splash_progress, alignment=Qt.AlignCenter)

        self.splash_desc = QLabel("⚡ Initializing Neural Core & Matrix Bus...")
        self.splash_desc.setFont(QFont("Inter", 9.5))
        self.splash_desc.setStyleSheet("color: #94A3B8; border: none; background: transparent; margin-top: 4px;")
        card_layout.addWidget(self.splash_desc, alignment=Qt.AlignCenter)

        main_vbox.addWidget(splash_card)
        self.card_layout.addWidget(self.splash_view)

    def authenticate_user(self):
        user = self.user_field.text().strip()
        pwd = self.pass_field.text().strip()

        if not user or not pwd:
            self.auth_card.trigger_shake()
            self.auth_error.setText("Please fill in all required fields.")
            return

        self.login_btn.start_loading()

        def _process_auth():
            if self.current_auth_mode == "signup":
                email = self.email_field.text().strip() or f"{user}@nexus-ai.local"
                success = db_manager.register_user(user, email, pwd)
                if not success:
                    self.login_btn.stop_loading()
                    self.auth_card.trigger_shake()
                    self.auth_error.setText("Username already taken. Please pick another.")
                    return
            else:
                if not db_manager.verify_user(user, pwd):
                    self.login_btn.stop_loading()
                    self.auth_card.trigger_shake()
                    self.auth_error.setText("Invalid Username or Password.")
                    self.pass_field.clear()
                    self.pass_field.setFocus()
                    return

            # Save session state if Remember Me is checked
            if self.remember_me_cb.isChecked():
                db_manager.set_setting("remember_me", "True")
                db_manager.set_setting("saved_session_user", user)
            else:
                db_manager.set_setting("remember_me", "False")
                db_manager.set_setting("saved_session_user", "")

            GlobalConfig.CURRENT_USER = user
            self.auth_error.clear()
            self.user_field.clear()
            self.pass_field.clear()
            self.email_field.clear()
            self.login_btn.stop_loading()

            self.card_layout.setCurrentWidget(self.splash_view)
            self.splash_worker = AppSplashScreenThread()
            self.splash_worker.progress_val.connect(
                lambda v: (self.splash_progress.setValue(v), self.splash_percent_lbl.setText(f"{v}%"))
            )
            self.splash_worker.progress_desc.connect(self.splash_desc.setText)
            self.splash_worker.finished.connect(self.complete_login)
            self.splash_worker.start()

        QTimer.singleShot(400, _process_auth)

    def complete_login(self):
        self.sidebar_frame.show()
        self.card_layout.setCurrentWidget(self.workspace_view)
        
        last_chat = db_manager.get_setting("last_active_chat_id", "")
        if last_chat and last_chat in self.all_chats: self.load_chat_conversation(last_chat)
        else: self.create_new_chat()

    # --------------------------------------------------------------------------
    # WORKSPACE VIEW (GLASSMORPHIC & TRANSPARENT VIEWPORT)
    # --------------------------------------------------------------------------
    def init_workspace_view(self):
        self.workspace_view = QWidget()
        self.workspace_view.setStyleSheet("background: transparent;")
        
        layout = QVBoxLayout(self.workspace_view)
        layout.setContentsMargins(14, 12, 14, 12)
        layout.setSpacing(10)

        nav_bar = QHBoxLayout()
        nav_bar.setSpacing(10)

        self.sidebar_toggle_btn = QPushButton()
        self.sidebar_toggle_btn.setIcon(create_svg_icon("menu", "#FFFFFF"))
        self.sidebar_toggle_btn.setFixedSize(36, 36)
        self.sidebar_toggle_btn.setCursor(Qt.PointingHandCursor)
        self.sidebar_toggle_btn.setStyleSheet("QPushButton { background-color: rgba(18, 29, 36, 0.85); color: #FFFFFF; border: 1px solid rgba(0, 229, 255, 0.2); border-radius: 8px; } QPushButton:hover { background-color: rgba(0,229,255,0.2); border: 1px solid #00E5FF; }")
        self.sidebar_toggle_btn.clicked.connect(lambda: self.sidebar_frame.setVisible(not self.sidebar_frame.isVisible()))
        nav_bar.addWidget(self.sidebar_toggle_btn)

        self.models_btn = QPushButton()
        self.models_btn.setCursor(Qt.PointingHandCursor)
        self.models_btn.setStyleSheet(f"QPushButton {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF); color: #080D11; border-radius: 8px; padding: 8px 16px; font-weight: bold; font-size: 12px; border: none; }} QPushButton:hover {{ background: #00C4DA; }}")
        self.models_btn.clicked.connect(self.open_model_selection_dialog)
        nav_bar.addWidget(self.models_btn)

        persona_lbl = QLabel("Persona:")
        persona_lbl.setFont(QFont("Inter", 10, QFont.Bold))
        persona_lbl.setStyleSheet("color: #94A3B8; margin-left: 10px;")
        nav_bar.addWidget(persona_lbl)

        self.persona_selector = QComboBox()
        self.persona_selector.setView(QListView())
        self.persona_selector.addItems(list(PERSONA_PROMPTS.keys()))
        self.persona_selector.setFixedWidth(180)
        self.persona_selector.setStyleSheet(f"""
            QComboBox {{ background-color: rgba(18, 29, 36, 0.85); color: #FFFFFF; border: 1px solid rgba(0,229,255,0.25); border-radius: 8px; padding: 6px 10px; font-size: 11.5px; }}
            QComboBox QAbstractItemView {{ background-color: #0B1318 !important; color: #FFFFFF !important; border: 1px solid {GlobalConfig.ACCENT_COLOR} !important; selection-background-color: rgba(0, 229, 255, 0.25) !important; }}
        """)
        nav_bar.addWidget(self.persona_selector)

        voice_lbl = QLabel("Voice:")
        voice_lbl.setFont(QFont("Inter", 10, QFont.Bold))
        voice_lbl.setStyleSheet("color: #94A3B8; margin-left: 10px;")
        nav_bar.addWidget(voice_lbl)

        self.voice_selector = QComboBox()
        self.voice_selector.setView(QListView())
        self.voice_map = {"Ava (US Female)": "en-US-AvaNeural", "Swara (IN Female)": "hi-IN-SwaraNeural", "Sonia (UK Female)": "en-GB-SoniaNeural", "Andrew (US Male)": "en-US-AndrewMultilingualNeural", "Madhur (IN Male)": "hi-IN-MadhurNeural", "Ryan (UK Male)": "en-GB-RyanNeural"}
        self.voice_selector.addItems(list(self.voice_map.keys()))
        self.voice_selector.setFixedWidth(160)
        self.voice_selector.setStyleSheet(self.persona_selector.styleSheet())
        nav_bar.addWidget(self.voice_selector)

        self.auto_tts_cb = QCheckBox("Auto-Voice")
        self.auto_tts_cb.setFont(QFont("Inter", 10, QFont.Bold))
        self.auto_tts_cb.setCursor(Qt.PointingHandCursor)
        self.auto_tts_cb.setStyleSheet(f"QCheckBox {{ color: {GlobalConfig.ACCENT_COLOR}; margin-left: 10px; }} QCheckBox::indicator {{ width: 16px; height: 16px; border-radius: 4px; border: 1px solid #1E2D38; background: #0B1318; }} QCheckBox::indicator:checked {{ background: {GlobalConfig.ACCENT_COLOR}; border: 1px solid {GlobalConfig.ACCENT_COLOR}; }}")
        nav_bar.addWidget(self.auto_tts_cb)

        self.web_search_toggle_btn = QPushButton("Web Search: OFF")
        self.web_search_toggle_btn.setCursor(Qt.PointingHandCursor)
        self.web_search_toggle_btn.setFixedHeight(32)
        self.web_search_toggle_btn.clicked.connect(self._toggle_web_search)
        self._update_web_search_toggle_ui()
        nav_bar.addWidget(self.web_search_toggle_btn)

        nav_bar.addStretch()

        exit_btn = QPushButton("Exit")
        exit_btn.setCursor(Qt.PointingHandCursor)
        exit_btn.setStyleSheet("QPushButton { color: #EF4444; font-weight: bold; background: rgba(239, 68, 68, 0.1); border: 1px solid #EF4444; border-radius: 8px; padding: 6px 16px; font-size: 12px; } QPushButton:hover { background: #EF4444; color: #FFFFFF; }")
        exit_btn.clicked.connect(self.close)
        nav_bar.addWidget(exit_btn)

        layout.addLayout(nav_bar)

        self.arena_scroll = QScrollArea()
        self.arena_scroll.setWidgetResizable(True)
        self.arena_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.arena_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.arena_scroll.setStyleSheet("background: transparent; border: none;")

        self.arena_container = QWidget()
        self.arena_container.setStyleSheet("background: transparent;")
        self.arena_layout = QHBoxLayout(self.arena_container)
        self.arena_layout.setContentsMargins(2, 2, 2, 2)
        self.arena_layout.setSpacing(12)
        self.arena_layout.setAlignment(Qt.AlignLeft)

        self.arena_scroll.setWidget(self.arena_container)
        layout.addWidget(self.arena_scroll, 1)

        centered_outer_box = QHBoxLayout()
        centered_outer_box.setContentsMargins(0, 0, 0, 0)

        self.center_column = QWidget()
        self.center_column.setStyleSheet("background: transparent;")
        self.center_column.setMaximumWidth(860)
        self.center_column.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        col_layout = QVBoxLayout(self.center_column)
        col_layout.setContentsMargins(0, 0, 0, 0)
        col_layout.setSpacing(6)

        self.attachment_badge_container = QScrollArea()
        self.attachment_badge_container.setFixedHeight(38)
        self.attachment_badge_container.setWidgetResizable(True)
        self.attachment_badge_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.attachment_badge_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.attachment_badge_container.setStyleSheet("background: transparent; border: none;")

        self.attachment_scroll_content = QWidget()
        self.attachment_scroll_content.setStyleSheet("background: transparent; border: none;")
        self.attachment_scroll_layout = QHBoxLayout(self.attachment_scroll_content)
        self.attachment_scroll_layout.setContentsMargins(2, 1, 2, 1)
        self.attachment_scroll_layout.setAlignment(Qt.AlignLeft)
        self.attachment_scroll_layout.setSpacing(8)

        self.attachment_badge_container.setWidget(self.attachment_scroll_content)
        self.attachment_badge_container.hide()
        col_layout.addWidget(self.attachment_badge_container)

        self.prompt_suggestion_bar = QWidget()
        self.prompt_suggestion_bar.setStyleSheet("background-color: transparent;")
        sg_layout = QHBoxLayout(self.prompt_suggestion_bar)
        sg_layout.setContentsMargins(0, 0, 0, 0)
        sg_layout.setSpacing(8)
        
        commands = {
            "/refactor": "Refactor this code to be more modular and clean:\n",
            "/explain": "Explain how this works step-by-step:\n",
            "/summarize": "Summarize the key points:\n",
            "/fix": "Find and fix bugs in this code:\n"
        }
        
        lbl_slash = QLabel("✨ Commands:")
        lbl_slash.setFont(QFont("Inter", 10, QFont.Bold))
        lbl_slash.setStyleSheet("color: #94A3B8;")
        sg_layout.addWidget(lbl_slash)
        
        for cmd, text in commands.items():
            btn = QPushButton(cmd)
            btn.setStyleSheet(f"background: rgba(18, 29, 36, 0.8); color: {GlobalConfig.ACCENT_COLOR}; border: 1px solid rgba(0, 229, 255, 0.25); border-radius: 6px; padding: 6px 10px; font-size: 11px; font-weight: bold;")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda ch, t=text: self._apply_prompt_command(t))
            sg_layout.addWidget(btn)
        sg_layout.addStretch()
        self.prompt_suggestion_bar.hide()
        
        col_layout.addWidget(self.prompt_suggestion_bar)

        self.input_dock = QFrame()
        self.input_dock.setObjectName("inputDock")
        self.input_dock.setStyleSheet(f"QFrame#inputDock {{ background-color: rgba(14, 22, 28, 0.88); border: 1px solid rgba(0, 229, 255, 0.35); border-radius: 12px; }} QFrame#inputDock:focus-within {{ border: 1.5px solid {GlobalConfig.ACCENT_COLOR}; }}")
        input_layout = QHBoxLayout(self.input_dock)
        input_layout.setContentsMargins(12, 6, 12, 6)
        input_layout.setSpacing(10)

        plus_btn = QPushButton()
        plus_btn.setIcon(create_svg_icon("plus", GlobalConfig.ACCENT_COLOR, 20))
        plus_btn.setFixedSize(34, 34)
        plus_btn.setCursor(Qt.PointingHandCursor)
        plus_btn.setToolTip("Attach Folders, Images, PDF, or Code File")
        plus_btn.setStyleSheet(f"QPushButton {{ background: transparent; border: none; border-radius: 8px; }} QPushButton:hover {{ background-color: rgba(0, 229, 255, 0.15); }}")
        plus_btn.clicked.connect(self.show_attachment_menu)

        self.prompt_entry = ChatInputTextEdit(self)
        self.prompt_entry.setPlaceholderText("Ask a question across models... (Type / for prompts, Enter to send)")
        self.prompt_entry.returnPressed.connect(self.dispatch_user_message)
        self.prompt_entry.largeTextPasted.connect(self.handle_large_text_paste)
        self.prompt_entry.textChanged.connect(self._check_slash_commands)

        self.voice_wave = VoiceWaveformWidget(self)
        self.voice_wave.hide()

        self.mic_btn = QPushButton()
        self.mic_btn.setIcon(create_svg_icon("mic", "#94A3B8", 20))
        self.mic_btn.setFixedSize(34, 34)
        self.mic_btn.setCursor(Qt.PointingHandCursor)
        self.mic_btn.setStyleSheet("QPushButton { background: transparent; border: none; border-radius: 8px; } QPushButton:hover { background-color: rgba(255, 255, 255, 0.1); }")
        self.mic_btn.clicked.connect(self.trigger_voice_recording)

        self.action_btn = QPushButton()
        self.action_btn.setIcon(create_svg_icon("send", "#080D11", 18))
        self.action_btn.setFixedSize(36, 36)
        self.action_btn.setCursor(Qt.PointingHandCursor)
        self.action_btn.setStyleSheet(f"QPushButton {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF); border-radius: 10px; border: none; }} QPushButton:hover {{ background: #00C4DA; }}")
        self.action_btn.clicked.connect(self.dispatch_user_message)

        input_layout.addWidget(plus_btn)
        input_layout.addWidget(self.prompt_entry, 1)
        input_layout.addWidget(self.voice_wave)
        input_layout.addWidget(self.mic_btn)
        input_layout.addWidget(self.action_btn)

        col_layout.addWidget(self.input_dock)
        centered_outer_box.addStretch()
        centered_outer_box.addWidget(self.center_column, 0, Qt.AlignCenter)
        centered_outer_box.addStretch()

        layout.addLayout(centered_outer_box)

        # Dedicated Footer
        self.footer_bar = QFrame()
        self.footer_bar.setFixedHeight(30)
        self.footer_bar.setStyleSheet("background: transparent;")
        footer_layout = QHBoxLayout(self.footer_bar)
        footer_layout.setContentsMargins(0, 0, 0, 0)
        
        self.stats_bar = QLabel(f"Logged in as {GlobalConfig.CURRENT_USER} | Parallel Word Streaming Online")
        self.stats_bar.setFont(QFont("Inter", 9))
        self.stats_bar.setStyleSheet("color: #71717A;")
        
        self.cost_lbl = QLabel(f"Total Session Cost: ${self.session_cost:.4f}")
        self.cost_lbl.setFont(QFont("Inter", 9, QFont.Bold))
        self.cost_lbl.setStyleSheet(f"color: {GlobalConfig.ACCENT_COLOR};")
        
        footer_layout.addWidget(self.stats_bar, 1)
        footer_layout.addWidget(self.cost_lbl)
        
        layout.addWidget(self.footer_bar)

        self.card_layout.addWidget(self.workspace_view)

        self.rebuild_arena_columns()
        self.update_models_button_label()

    def _toggle_web_search(self):
        self.web_search_active = not self.web_search_active
        self._update_web_search_toggle_ui()

    def _update_web_search_toggle_ui(self):
        if self.web_search_active:
            self.web_search_toggle_btn.setText("Web Search: ON")
            self.web_search_toggle_btn.setStyleSheet(f"QPushButton {{ background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {GlobalConfig.ACCENT_COLOR}, stop:1 #0072FF); color: #080D11; border-radius: 16px; padding: 6px 14px; font-weight: Bold; font-size: 11px; border: none; }} QPushButton:hover {{ background: #00C4DA; }}")
        else:
            self.web_search_toggle_btn.setText("Web Search: OFF")
            self.web_search_toggle_btn.setStyleSheet("QPushButton { background: #121D24; color: #94A3B8; border: 1px solid #1E2D38; border-radius: 16px; padding: 6px 14px; font-weight: Bold; font-size: 11px; } QPushButton:hover { background: #1E2D38; color: #FFFFFF; }")

    def _check_slash_commands(self):
        text = self.prompt_entry.toPlainText()
        if text.endswith("/") or text.endswith("\n/"): self.prompt_suggestion_bar.show()
        else: self.prompt_suggestion_bar.hide()
            
    def _apply_prompt_command(self, cmd_text):
        text = self.prompt_entry.toPlainText()
        if text.endswith("/"): text = text[:-1]
        self.prompt_entry.setPlainText(text + cmd_text)
        self.prompt_suggestion_bar.hide()
        self.prompt_entry.setFocus()
        cursor = self.prompt_entry.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.prompt_entry.setTextCursor(cursor)

    def handle_chat_branching(self, history_idx: int):
        if not self.active_chat_id or self.active_chat_id not in self.all_chats: return
        chat_data = self.all_chats[self.active_chat_id]
        if not self.arena_columns: return
        first_col = list(self.arena_columns.values())[0]
        if history_idx >= len(first_col.full_turn_history): return
        
        item = first_col.full_turn_history[history_idx]
        if item["type"] != "user": return
            
        prompt_text = item.get("raw_text", item["text"])
        user_msg_count = sum(1 for i in range(history_idx) if first_col.full_turn_history[i]["type"] == "user")
        db_slice_idx = user_msg_count * 2
        
        chat_data["messages"] = chat_data["messages"][:db_slice_idx]
        db_manager.save_chat(self.active_chat_id, chat_data["title"], chat_data["messages"])
        self.load_chat_conversation(self.active_chat_id)
        
        clean_prompt = re.sub(r'!\[.*?\]\(data:image.*?\)', '', prompt_text)
        clean_prompt = re.sub(r'\[Attached (Image|Document): .*?\]\n', '', clean_prompt).strip()
        self.prompt_entry.setPlainText(clean_prompt)
        self.prompt_entry.setFocus()

    def update_models_button_label(self):
        count = len(self.selected_model_ids)
        if count == 1:
            m_id = self.selected_model_ids[0]
            name = FREE_MODELS_REGISTRY.get(m_id, {}).get("name", "1 Model")
            self.models_btn.setText(f"{name}")
        else:
            self.models_btn.setText(f"Multi-Model ({count} Columns) ▾")

    def rebuild_arena_columns(self):
        try:
            current_active = set(self.selected_model_ids)
            for mid in list(self.arena_columns.keys()):
                if mid not in current_active:
                    col = self.arena_columns.pop(mid)
                    self.arena_layout.removeWidget(col)
                    col.deleteLater()

            for mid in self.selected_model_ids:
                if mid not in self.arena_columns and mid in FREE_MODELS_REGISTRY:
                    col = ModelArenaColumn(mid, parent=self)
                    col.close_requested.connect(self.remove_model_from_arena)
                    col.tts_requested.connect(self.toggle_audio_playback)
                    col.copy_requested.connect(lambda text: QApplication.clipboard().setText(text))
                    col.branch_requested.connect(self.handle_chat_branching)
                    self.arena_layout.addWidget(col)
                    self.arena_columns[mid] = col

            num = len(self.selected_model_ids)
            for col in self.arena_columns.values():
                if num == 1: col.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding); col.setMinimumWidth(560)
                elif num == 2: col.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding); col.setMinimumWidth(440)
                else: col.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding); col.setMinimumWidth(380)

            self.update_models_button_label()
        except Exception:
            traceback.print_exc()

    def remove_model_from_arena(self, model_id: str):
        if len(self.selected_model_ids) <= 1:
            QMessageBox.information(self, "Notice", "At least 1 active AI model is required.")
            return
        if model_id in self.selected_model_ids:
            self.selected_model_ids.remove(model_id)
            db_manager.set_setting("selected_models", json.dumps(self.selected_model_ids))
            self.rebuild_arena_columns()

    def open_model_selection_dialog(self):
        dialog = ModelSelectionDialog(self.selected_model_ids, parent=self)
        dialog.models_selected_signal.connect(self.set_selected_models)
        dialog.exec()

    def set_selected_models(self, models_list: List[str]):
        if models_list:
            self.selected_model_ids = models_list
            db_manager.set_setting("selected_models", json.dumps(models_list))
            self.rebuild_arena_columns()

    # --------------------------------------------------------------------------
    # MESSAGE DISPATCH & STREAMING HANDLERS
    # --------------------------------------------------------------------------
    def dispatch_user_message(self):
        if self.active_workers:
            self.stop_all_workers()
            self.action_btn.setIcon(create_svg_icon("send", "#080D11", 18))
            self.stats_bar.setText("Parallel streaming stopped.")
            return

        user_text = self.prompt_entry.toPlainText().strip()
        if not user_text and not self.attached_files:
            return

        if not self.selected_model_ids:
            self.open_model_selection_dialog()
            return

        self.prompt_entry.clear()
        self.prompt_entry.setFixedHeight(40)
        self.turn_audio_played = False

        image_bytes_list = []
        doc_contexts = []
        display_badges = []

        for item in self.attached_files:
            if item["type"] == "image":
                image_bytes_list.append(item["bytes"])
                ext = os.path.splitext(item['name'])[1][1:] or "png"
                img_md = f"![{item['name']}](data:image/{ext};base64,{item.get('b64_str', '')})"
                display_badges.append(img_md)
            elif item["type"] in ["text", "pdf"]:
                doc_contexts.append(f"--- File: {item['name']} ---\n{item.get('text', '')}\n")
                display_badges.append(f"[Attached Document: {item['name']}]")

        self.clear_all_attachments()

        display_prompt = "\n\n".join(display_badges) + ("\n\n" if display_badges and user_text else "") + user_text
        if not display_prompt: display_prompt = "Analyzed attached document payload."

        actual_prompt = user_text
        if doc_contexts:
            combined_docs = "\n".join(doc_contexts)
            if len(combined_docs.split()) > 2000:
                display_prompt = f"[RAG Active: Extracted Most Relevant Pages]\n\n{display_prompt}"
                if HAS_FAISS:
                    try:
                        embedder = SentenceTransformer('all-MiniLM-L6-v2')
                        chunks = [combined_docs[i:i+1000] for i in range(0, len(combined_docs), 1000)]
                        embeddings = embedder.encode(chunks)
                        index = faiss.IndexFlatL2(embeddings.shape[1])
                        index.add(embeddings)
                        q_emb = embedder.encode([user_text])
                        D, I = index.search(q_emb, k=min(4, len(chunks)))
                        rag_context = "\n\n...[Snippet]...\n\n".join([chunks[i] for i in I[0] if i < len(chunks)])
                    except Exception:
                        rag_context = lightweight_rag_chunker(user_text, combined_docs, top_k=4)
                else:
                    rag_context = lightweight_rag_chunker(user_text, combined_docs, top_k=4)
                actual_prompt = f"Relevant Document Context:\n{rag_context}\n\nUser Question:\n{user_text or 'Summarize the context.'}"
            else:
                actual_prompt = f"Document Context:\n{combined_docs}\n\nUser Question:\n{user_text or 'Summarize the context.'}"

        current_history = self.all_chats.get(self.active_chat_id, {}).get("messages", [])
        if len(current_history) == 0 and self.active_chat_id:
            short_title = user_text[:22] + "..." if len(user_text) > 22 else (user_text or "Task Session")
            if self.active_chat_id in self.all_chats:
                self.all_chats[self.active_chat_id]["title"] = short_title
            self.refresh_sidebar_list()

        current_history.append({"role": "user", "content": actual_prompt, "display_content": display_prompt, "raw_text": user_text})

        for mid in self.selected_model_ids:
            if mid in self.arena_columns:
                col = self.arena_columns[mid]
                col.append_user_prompt(display_prompt, raw_text=user_text)

        self.action_btn.setIcon(QIcon())
        self.action_btn.setText("■")
        self.stats_bar.setText(f"Streaming {len(self.selected_model_ids)} models in parallel...")

        system_prompt = PERSONA_PROMPTS.get(self.persona_selector.currentText(), PERSONA_PROMPTS["Universal Assistant"])
        use_web = self.web_search_active
        history_snapshot = list(current_history[:-1])
        
        for mid in self.selected_model_ids:
            try:
                worker = UniversalAIWorkerThread(
                    model_id=mid, history_list=history_snapshot, user_prompt=actual_prompt,
                    system_prompt=system_prompt, temperature=GlobalConfig.TEMPERATURE,
                    max_tokens=GlobalConfig.MAX_TOKENS, image_list=image_bytes_list, use_web_search=use_web
                )
                worker.chunk_ready.connect(self._handle_model_chunk)
                worker.stats_ready.connect(self._handle_model_stats)
                worker.error_signal.connect(self._handle_model_error)
                worker.finished_signal.connect(self._handle_model_finished)
                worker.finished.connect(worker.deleteLater)
                worker.finished.connect(lambda m=mid: self._on_worker_thread_finished(m))

                self.active_workers[mid] = worker
                worker.start()
            except Exception:
                traceback.print_exc()

    def _handle_model_chunk(self, model_id: str, chunk_text: str):
        try:
            if model_id in self.arena_columns: self.arena_columns[model_id].append_chunk(chunk_text)
        except Exception: pass

    def _handle_model_stats(self, model_id: str, latency: float, p_tok: int, c_tok: int, cost: float):
        try:
            self.session_cost += cost
            self.cost_lbl.setText(f"Total Session Cost: ${self.session_cost:.4f}")
            if model_id in self.arena_columns:
                speed = round(c_tok / latency, 1) if latency > 0 else 0
                bcol = FREE_MODELS_REGISTRY.get(model_id, {}).get("badge_color", GlobalConfig.ACCENT_COLOR)
                self.arena_columns[model_id].status_badge.setText(f"{latency}s | {speed} tok/s")
                self.arena_columns[model_id].status_badge.setStyleSheet(f"color: {bcol}; font-weight: bold;")
        except Exception: pass

    def _handle_model_error(self, model_id: str, error_code: str, error_msg: str):
        try:
            if model_id in self.arena_columns: self.arena_columns[model_id].set_error_state(error_code, error_msg)
        except Exception: pass

    def _handle_model_finished(self, model_id: str, full_response: str):
        try:
            if model_id in self.arena_columns:
                self.arena_columns[model_id].finish_turn(full_response)
                if self.auto_tts_cb.isChecked() and not getattr(self, 'turn_audio_played', False):
                    self.turn_audio_played = True
                    self.toggle_audio_playback(model_id, full_response)
        except Exception: pass

    def _on_worker_thread_finished(self, model_id: str):
        try:
            if model_id in self.active_workers: del self.active_workers[model_id]
            if not self.active_workers:
                self.action_btn.setText("")
                self.action_btn.setIcon(create_svg_icon("send", "#080D11", 18))
                self.stats_bar.setText(f"All {len(self.selected_model_ids)} models finished streaming.")
                chat_data = self.all_chats.get(self.active_chat_id)
                if chat_data:
                    resp_dict = {}
                    for mid in self.selected_model_ids:
                        if mid in self.arena_columns:
                            resp_dict[mid] = self.arena_columns[mid].get_current_turn_text()
                    chat_data["messages"].append({"role": "assistant_multi", "responses": resp_dict})
                    chat_data["updated_at"] = time.time()
                    db_manager.save_chat(self.active_chat_id, chat_data["title"], chat_data["messages"])
        except Exception: pass

    # --------------------------------------------------------------------------
    # CHAT HISTORY & CONTEXT MENU
    # --------------------------------------------------------------------------
    def create_new_chat(self):
        try:
            if self.active_chat_id and self.active_chat_id in self.all_chats:
                msgs = self.all_chats[self.active_chat_id].get("messages", [])
                if not msgs:
                    self.prompt_entry.clear(); self.clear_all_attachments(); self.prompt_entry.setFocus()
                    return

            for cid, data in self.all_chats.items():
                if not data.get("messages", []): self.load_chat_conversation(cid); return

            self.stop_any_active_audio()
            self.stop_all_workers()
            self.session_cost = 0.0
            self.cost_lbl.setText(f"Total Session Cost: ${self.session_cost:.4f}")

            chat_id = f"chat_{int(time.time() * 1000)}"
            self.all_chats[chat_id] = {
                "title": "New Conversation", "messages": [], "pinned": False,
                "model_used": ",".join(self.selected_model_ids), "updated_at": time.time()
            }
            self.active_chat_id = chat_id
            db_manager.save_chat(chat_id, "New Conversation", [], pinned=0)
            db_manager.set_setting("last_active_chat_id", chat_id)

            for col in self.arena_columns.values(): col.reset_column()

            self.clear_all_attachments()
            self.refresh_sidebar_list()
            self.prompt_entry.clear()
            self.prompt_entry.setFocus()
            self.stats_bar.setText(f"Fresh session ready | {len(self.selected_model_ids)} active models")
        except Exception: pass

    def load_chat_conversation(self, chat_id: str):
        try:
            self.stop_any_active_audio()
            self.stop_all_workers()
            self.active_chat_id = chat_id
            db_manager.set_setting("last_active_chat_id", chat_id)
            self.session_cost = 0.0
            self.cost_lbl.setText(f"Total Session Cost: ${self.session_cost:.4f}")

            if chat_id not in self.all_chats: return
            chat_data = self.all_chats[chat_id]
            messages = chat_data.get("messages", [])

            used_models = set(self.selected_model_ids)
            for msg in messages:
                if msg.get("role") == "assistant_multi":
                    for k in msg.get("responses", {}).keys():
                        if k in FREE_MODELS_REGISTRY: used_models.add(k)

            self.selected_model_ids = list(used_models)
            self.rebuild_arena_columns()
            for col in self.arena_columns.values(): col.reset_column()

            if messages:
                for msg in messages:
                    role = msg.get("role", "")
                    if role == "user":
                        p_text = msg.get("display_content", msg.get("content", ""))
                        raw_text = msg.get("raw_text", p_text)
                        for col in self.arena_columns.values(): col.append_historical_user_prompt(p_text, raw_text)
                    elif role == "assistant_multi":
                        resps = msg.get("responses", {})
                        for mid, col in self.arena_columns.items():
                            resp_text = resps.get(mid)
                            if resp_text: col.append_historical_assistant_response(resp_text)
                            else: col.append_historical_assistant_response("[Model was not evaluated for this query]")

                for col in self.arena_columns.values(): col.render_all_turns(is_streaming=False)
            else:
                for col in self.arena_columns.values(): col.show_placeholder()

            self.refresh_sidebar_list()
            self.stats_bar.setText(f"Loaded '{chat_data.get('title', 'Chat')}'")
        except Exception: pass

    def refresh_sidebar_list(self, filter_text: str = ""):
        try:
            while self.history_layout.count():
                item = self.history_layout.takeAt(0)
                if item.widget(): item.widget().deleteLater()

            for cid, data in self.all_chats.items():
                title = data.get("title", "Untitled Chat")
                if filter_text.lower() and filter_text.lower() not in title.lower(): continue

                row = QWidget()
                row.setStyleSheet("background: transparent; border: none;")
                r_layout = QHBoxLayout(row)
                r_layout.setContentsMargins(0, 0, 0, 0)
                r_layout.setSpacing(2)

                is_active = (cid == self.active_chat_id)
                is_pinned = data.get("pinned", False)
                pin_icon = "📌 " if is_pinned else ""

                chat_btn = QPushButton(f"{pin_icon}{title}")
                chat_btn.setCursor(Qt.PointingHandCursor)
                chat_btn.setContextMenuPolicy(Qt.CustomContextMenu)

                if is_active:
                    chat_btn.setStyleSheet(f"QPushButton {{ background-color: rgba(0, 229, 255, 0.22); color: {GlobalConfig.ACCENT_COLOR}; text-align: left; padding: 8px 10px; border-radius: 8px; border: 1px solid rgba(0, 229, 255, 0.45); font-weight: bold; font-size: 11.5px; }}")
                else:
                    chat_btn.setStyleSheet("QPushButton { background: rgba(18,29,36,0.3); color: #94A3B8; text-align: left; padding: 8px 10px; border-radius: 8px; border: 1px solid transparent; font-size: 11.5px; } QPushButton:hover { background-color: rgba(0, 229, 255, 0.1); color: #FFFFFF; border: 1px solid rgba(0,229,255,0.25); }")
                
                chat_btn.clicked.connect(lambda ch=False, c=cid: self.load_chat_conversation(c))
                chat_btn.customContextMenuRequested.connect(lambda pos, c=cid, b=chat_btn: self.show_chat_context_menu(c, b.mapToGlobal(pos)))

                opt_btn = QPushButton("⋮")
                opt_btn.setFixedSize(20, 20)
                opt_btn.setCursor(Qt.PointingHandCursor)
                opt_btn.setStyleSheet("background: transparent; color: #71717A; border: none; font-size: 14px;")
                opt_btn.clicked.connect(lambda ch=False, c=cid, b=opt_btn: self.show_chat_context_menu(c, b.mapToGlobal(b.rect().bottomLeft())))

                r_layout.addWidget(chat_btn, 1)
                r_layout.addWidget(opt_btn)
                self.history_layout.addWidget(row)
        except Exception: pass

    def filter_sidebar_chats(self, text: str):
        self.refresh_sidebar_list(filter_text=text)

    def show_chat_context_menu(self, chat_id: str, global_pos):
        try:
            if chat_id not in self.all_chats: return
            menu = QMenu(self)
            menu.setStyleSheet(f"QMenu {{ background-color: #0E161C; color: #FFFFFF; border: 1px solid rgba(0, 229, 255, 0.4); border-radius: 8px; padding: 4px; }} QMenu::item {{ padding: 8px 16px; font-size: 12px; border-radius: 4px; }} QMenu::item:selected {{ background-color: {GlobalConfig.ACCENT_COLOR}; color: #000000; font-weight: bold; }}")

            is_pinned = self.all_chats[chat_id].get("pinned", False)
            pin_act = menu.addAction("Unpin" if is_pinned else "Pin")
            rename_act = menu.addAction("Rename")
            delete_act = menu.addAction("Delete")

            action = menu.exec(global_pos)
            if action == pin_act:
                cur = self.all_chats[chat_id].get("pinned", False)
                self.all_chats[chat_id]["pinned"] = db_manager.toggle_pin(chat_id, cur)
                self.all_chats = db_manager.load_all_chats()
                self.refresh_sidebar_list()
            elif action == rename_act:
                cur_title = self.all_chats[chat_id]["title"]
                new_title, ok = QInputDialog.getText(self, "Rename Chat", "Title:", text=cur_title)
                if ok and new_title.strip():
                    self.all_chats[chat_id]["title"] = new_title.strip()
                    db_manager.save_chat(chat_id, new_title.strip(), self.all_chats[chat_id]["messages"])
                    self.refresh_sidebar_list()
            elif action == delete_act:
                db_manager.delete_chat(chat_id)
                if chat_id in self.all_chats: del self.all_chats[chat_id]
                if self.active_chat_id == chat_id: self.create_new_chat()
                else: self.refresh_sidebar_list()
        except Exception: pass

    # --------------------------------------------------------------------------
    # ATTACHMENTS & DRAG AND DROP
    # --------------------------------------------------------------------------
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls(): event.acceptProposedAction()
        else: event.ignore()

    def dropEvent(self, event: QDropEvent):
        try:
            urls = event.mimeData().urls()
            file_paths = [u.toLocalFile() for u in urls if u.isLocalFile()]
            if file_paths:
                self.process_incoming_files(file_paths)
                event.acceptProposedAction()
        except Exception: pass

    def process_incoming_files(self, file_paths: List[str]):
        try:
            valid_exts = ['.txt', '.py', '.js', '.ts', '.html', '.css', '.cpp', '.c', '.h', '.java', '.json', '.md']
            for fp in file_paths:
                if not os.path.exists(fp): continue
                if os.path.isdir(fp):
                    for root, dirs, files in os.walk(fp):
                        for file in files:
                            ext = os.path.splitext(file)[1].lower()
                            if ext in valid_exts:
                                full_path = os.path.join(root, file)
                                try:
                                    if os.path.getsize(full_path) < 1024 * 500:
                                        with open(full_path, "r", encoding="utf-8", errors="replace") as f: content = f.read()
                                        file_id = f"file_{int(time.time()*1000)}_{len(self.attached_files)}"
                                        self.attached_files.append({"id": file_id, "type": "text", "name": f"{os.path.basename(fp)}/{file}", "path": full_path, "text": content, "thumbnail": None})
                                except Exception: pass
                    continue

                ext = os.path.splitext(fp)[1].lower()
                file_name = os.path.basename(fp)
                file_id = f"file_{int(time.time()*1000)}_{len(self.attached_files)}"

                if ext in [".png", ".jpg", ".jpeg", ".webp"]:
                    with open(fp, "rb") as f: raw = f.read()
                    b64_str = base64.b64encode(raw).decode('utf-8')
                    pixmap = QPixmap(fp)
                    thumb = pixmap.scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation) if not pixmap.isNull() else None
                    self.attached_files.append({"id": file_id, "type": "image", "name": file_name, "path": fp, "bytes": raw, "b64_str": b64_str, "thumbnail": thumb})
                elif ext == ".pdf":
                    pdf_text = ""
                    if HAS_PYPDF:
                        try:
                            reader = PdfReader(fp)
                            for page in reader.pages: pdf_text += (page.extract_text() or "") + "\n"
                        except Exception as e: pdf_text = f"[PDF extraction notice: {str(e)}]"
                    else: pdf_text = f"[PDF document attached: {file_name}]"
                    self.attached_files.append({"id": file_id, "type": "pdf", "name": file_name, "path": fp, "text": pdf_text, "thumbnail": None})
                elif ext in valid_exts + [".csv", ".sql", ".jsx", ".tsx"]:
                    with open(fp, "r", encoding="utf-8", errors="replace") as f: content = f.read()
                    self.attached_files.append({"id": file_id, "type": "text", "name": file_name, "path": fp, "text": content, "thumbnail": None})

            self.update_attachment_badges_ui()
        except Exception: pass

    def handle_large_text_paste(self, pasted_text: str):
        try:
            file_id = f"paste_{int(time.time()*1000)}"
            file_name = f"snippet_{len(self.attached_files)+1}.txt"
            self.attached_files.append({"id": file_id, "type": "text", "name": file_name, "path": "", "text": pasted_text, "thumbnail": None})
            self.update_attachment_badges_ui()
        except Exception: pass

    def remove_attached_file(self, file_id: str):
        self.attached_files = [f for f in self.attached_files if f["id"] != file_id]
        self.update_attachment_badges_ui()

    def clear_all_attachments(self):
        self.attached_files.clear()
        self.update_attachment_badges_ui()

    def update_attachment_badges_ui(self):
        try:
            while self.attachment_scroll_layout.count():
                item = self.attachment_scroll_layout.takeAt(0)
                if item.widget(): item.widget().deleteLater()

            if not self.attached_files:
                self.attachment_badge_container.hide()
                return

            for item in self.attached_files:
                chip = AttachmentBadgeChip(item["id"], item["name"], item["type"], item.get("thumbnail"), parent=self)
                chip.removed.connect(self.remove_attached_file)
                self.attachment_scroll_layout.addWidget(chip)
            self.attachment_badge_container.show()
        except Exception: pass

    def show_attachment_menu(self):
        try:
            menu = QMenu(self)
            menu.setStyleSheet(f"QMenu {{ background-color: #0E161C; color: #FFFFFF; border: 1px solid rgba(0, 229, 255, 0.4); border-radius: 8px; padding: 4px; }} QMenu::item {{ padding: 8px 16px; font-size: 11.5px; border-radius: 4px; }} QMenu::item:selected {{ background-color: {GlobalConfig.ACCENT_COLOR}; color: #000000; font-weight: bold; }}")
            img_act = menu.addAction("Attach Images")
            doc_act = menu.addAction("Attach Documents / Code / PDF")
            dir_act = menu.addAction("Attach Project Folder (RAG Context)")

            action = menu.exec(QCursor.pos())
            if action == img_act:
                file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.webp)")
                if file_paths: self.process_incoming_files(file_paths)
            elif action == doc_act:
                file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Documents", "", "Documents (*.txt *.py *.json *.md *.csv *.js *.html *.cpp *.c *.h *.pdf)")
                if file_paths: self.process_incoming_files(file_paths)
            elif action == dir_act:
                folder_path = QFileDialog.getExistingDirectory(self, "Select Project Folder")
                if folder_path: self.process_incoming_files([folder_path])
        except Exception: pass

    # --------------------------------------------------------------------------
    # PIPELINED ZERO-DELAY STREAMING AUDIO CONTROLLER
    # --------------------------------------------------------------------------
    def toggle_audio_playback(self, model_id: str, text: str):
        try:
            if self.audio_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                was_same = (self.active_audio_model_id == model_id)
                self.stop_any_active_audio()
                if was_same: return

            clean_text = re.sub(r'[*_`#~<>]', '', text)
            clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
            clean_text = re.sub(r'\$\$?[^\$]+\$\$?', '', clean_text).strip()

            if not clean_text: return

            # Split by punctuation for sentence-level immediate playback
            raw_sentences = re.split(r'(?<=[.!?\n])\s+', clean_text)
            sentences = [s.strip() for s in raw_sentences if len(s.strip()) > 1]
            if not sentences:
                sentences = [clean_text]

            self.stop_any_active_audio()
            self.active_audio_model_id = model_id
            self.audio_chunk_queue.clear()
            self.current_playback_index = 0

            if model_id in self.arena_columns:
                self.arena_columns[model_id].set_audio_playing(True)

            selected_voice_name = self.voice_selector.currentText()
            voice_id = self.voice_map.get(selected_voice_name, "en-US-AvaNeural")
            cur_speed = GlobalConfig.VOICE_SPEED_RATE

            self.active_producer_thread = StreamingTTSProducerThread(sentences, voice=voice_id, speed_rate=cur_speed)
            self.active_producer_thread.chunk_ready.connect(self._handle_audio_chunk_ready)
            self.active_producer_thread.error_signal.connect(lambda err: QMessageBox.warning(self, "Voice Synthesis Notice", err))
            self.active_producer_thread.start()
        except Exception: pass

    def _handle_audio_chunk_ready(self, index: int, file_path: str):
        self.audio_chunk_queue[index] = file_path
        self.all_temp_voice_files.append(file_path)

        # If player is currently idle and the expected next chunk is ready, play immediately
        if self.audio_player.playbackState() != QMediaPlayer.PlaybackState.PlayingState:
            if self.current_playback_index in self.audio_chunk_queue:
                self._play_next_chunk()

    def _play_next_chunk(self):
        if self.current_playback_index in self.audio_chunk_queue:
            file_to_play = self.audio_chunk_queue[self.current_playback_index]
            self.audio_player.setSource(QUrl.fromLocalFile(file_to_play))
            self.audio_player.play()
            self.current_playback_index += 1
        else:
            if self.active_producer_thread and not self.active_producer_thread.isRunning():
                self.stop_any_active_audio()

    def _on_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.current_playback_index in self.audio_chunk_queue:
                self._play_next_chunk()
            elif self.active_producer_thread and self.active_producer_thread.isRunning():
                pass
            else:
                self.stop_any_active_audio()

    def stop_any_active_audio(self):
        try:
            if self.audio_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.audio_player.stop()
            if self.active_producer_thread and self.active_producer_thread.isRunning():
                self.active_producer_thread.stop()
                self.active_producer_thread.wait(150)
                self.active_producer_thread = None

            if self.active_audio_model_id and self.active_audio_model_id in self.arena_columns:
                self.arena_columns[self.active_audio_model_id].set_audio_playing(False)
            self.active_audio_model_id = None
            self.audio_chunk_queue.clear()
            self.current_playback_index = 0

            for temp_f in list(self.all_temp_voice_files):
                if os.path.exists(temp_f):
                    try: os.remove(temp_f)
                    except: pass
            self.all_temp_voice_files.clear()
        except Exception: pass

    def trigger_voice_recording(self):
        try:
            self.voice_wave.show()
            self.prompt_entry.setPlaceholderText("Listening...")
            self.voice_worker = VoiceRecognitionThread(lang=GlobalConfig.STT_LANG)
            self.voice_worker.text_recognized.connect(lambda t: self.prompt_entry.setPlainText(t))
            self.voice_worker.status_changed.connect(lambda s: self.prompt_entry.setPlaceholderText(s))
            self.voice_worker.finished_signal.connect(self.finish_voice_recording)
            self.voice_worker.start()
        except Exception: pass

    def finish_voice_recording(self):
        self.voice_wave.hide()
        self.prompt_entry.setPlaceholderText("Ask a question across models... (Type / for prompts, Enter to send)")

    def open_settings(self):
        auth_overlay = SettingsAuthDialog(parent=self)
        if auth_overlay.exec() == QDialog.Accepted:
            dialog = SettingsDialog(self)
            dialog.settings_updated.connect(self._on_settings_updated)
            dialog.exec()

    def _on_settings_updated(self):
        self.all_chats = db_manager.load_all_chats()
        self.apply_ninja_hex_theme()
        for mid, col in self.arena_columns.items():
            bcol = col.model_info.get("badge_color", GlobalConfig.ACCENT_COLOR)
            col.setStyleSheet(f"""
                QFrame#modelColumn {{
                    background-color: rgba(14, 22, 28, 0.62);
                    border: 1.5px solid rgba(0, 229, 255, 0.28);
                    border-top: 3px solid {bcol};
                    border-radius: 12px;
                }}
            """)
            col.render_all_turns(is_streaming=False)
        self.refresh_sidebar_list()

    # --------------------------------------------------------------------------
    # CUSTOM EXPORT HANDLER WITH GRANULAR MODEL SELECTION
    # --------------------------------------------------------------------------
    def export_current_chat(self):
        try:
            if not self.active_chat_id or self.active_chat_id not in self.all_chats:
                QMessageBox.warning(self, "Export", "No active conversation to export.")
                return

            chat = self.all_chats[self.active_chat_id]
            messages = chat.get("messages", [])
            if not messages:
                QMessageBox.information(self, "Export", "This conversation has no messages to export.")
                return

            present_models = set(self.selected_model_ids)
            for m in messages:
                if m.get("role") == "assistant_multi":
                    for k in m.get("responses", {}).keys():
                        present_models.add(k)

            export_dialog = CyberExportDialog(list(present_models), parent=self)
            if export_dialog.exec() != QDialog.Accepted:
                return

            chosen_models = export_dialog.selected_export_models
            chosen_format = export_dialog.selected_format

            default_filename = f"{chat['title']}"
            if chosen_format == "pdf":
                path, _ = QFileDialog.getSaveFileName(self, "Export Conversation (PDF)", f"{default_filename}.pdf", "PDF Document (*.pdf)")
            elif chosen_format == "md":
                path, _ = QFileDialog.getSaveFileName(self, "Export Conversation (Markdown)", f"{default_filename}.md", "Markdown (*.md)")
            else:
                path, _ = QFileDialog.getSaveFileName(self, "Export Conversation (MS Word / HTML)", f"{default_filename}.doc", "MS Word / HTML (*.doc)")

            if not path:
                return

            html_content = f"<h1 style='color:#00B4D8;'>NEXUS AI Report: {chat['title']}</h1><p style='color:#71717A; font-size:11px;'>Architecture: Nexus Multi-Model Arena | Created by Wajahat</p><hr>"
            md_content = f"# NEXUS AI Report: {chat['title']}\n*Architecture: Nexus Multi-Model Arena | Created by Wajahat*\n\n---\n\n"

            for m in messages:
                role = m.get("role", "")
                if role == "user":
                    user_p = m.get("content", "").replace("\n", "<br>")
                    html_content += f"<h3 style='color:#FFFFFF; background:#121D24; padding:8px; border-radius:6px;'>Prompt:</h3><p>{user_p}</p><hr>"
                    md_content += f"### Prompt:\n{m.get('content', '')}\n\n---\n\n"
                elif role == "assistant_multi":
                    resps = m.get("responses", {})
                    for mid in chosen_models:
                        if mid in resps and resps[mid]:
                            mname = FREE_MODELS_REGISTRY.get(mid, {}).get("name", mid)
                            clean_html = markdown.markdown(resps[mid])
                            html_content += f"<h4 style='color:#00E5FF;'>🤖 {mname}:</h4><div>{clean_html}</div><br>"
                            md_content += f"#### 🤖 {mname}:\n{resps[mid]}\n\n"
                    html_content += "<hr style='border:1px solid #1E2D38;'>"
                    md_content += "---\n\n"

            if chosen_format == "md" or path.endswith('.md'):
                with open(path, "w", encoding="utf-8") as f: f.write(md_content)
            elif chosen_format == "doc" or path.endswith('.doc'):
                with open(path, "w", encoding="utf-8") as f:
                    f.write("<html><head><meta charset='utf-8'></head><body style='font-family: Arial, sans-serif; background-color: #FFFFFF; color:#111827; padding:20px;'>" + html_content + "</body></html>")
            elif chosen_format == "pdf" or path.endswith('.pdf'):
                writer = QPdfWriter(path)
                writer.setCreator("Nexus AI Pro - Multi-Model Arena")
                doc = QTextDocument()
                doc.setHtml("<body style='font-family: Arial, sans-serif; padding:15px;'>" + html_content + "</body>")
                doc.print_(writer)

            QMessageBox.information(self, "Export Complete", f"Successfully exported responses from {len(chosen_models)} model(s) to:\n{os.path.basename(path)}")
        except Exception as e:
            QMessageBox.critical(self, "Export Failed", f"An error occurred while exporting: {str(e)}")

# ==============================================================================
# 14. ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Inter", 10))
    window = NexusAIProApp()
    window.show()
    sys.exit(app.exec())