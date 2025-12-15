# Neeva - AI Mental Wellness Companion

A production-ready mental wellness application for young Indians, combining mood tracking, AI therapy, CBT exercises, and community support.

## 🚀 Quick Start

### Backend
```bash
cd backend
.\venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
**Backend URL:** http://localhost:8000  
**API Docs:** http://localhost:8000/docs

### Frontend
```bash
cd frontend
npm run dev
```
**Frontend URL:** http://localhost:5173

## ✨ Features

- ✅ **User Authentication** - JWT-based secure login/register
- ✅ **Mood Tracking** - 5-level emotion scale with notes
- ✅ **AI Chat** - Groq-powered empathetic therapist
- ✅ **Wellness Exercises** - 6 guided meditation sessions
- ✅ **Crisis Support** - Emergency resources and hotlines
- ✅ **Responsive Design** - Desktop sidebar + mobile bottom nav

## 🛠️ Tech Stack

**Backend:** FastAPI, PostgreSQL (Supabase), Groq AI  
**Frontend:** React 19, TypeScript, Tailwind CSS, TanStack Query  
**Security:** JWT, bcrypt, AES-256 ready

## 📖 Documentation

See [walkthrough.md](C:\Users\diyab\.gemini\antigravity\brain\c187bc08-598d-4eae-9d30-1505b9664b08\walkthrough.md) for complete documentation.

## 🔐 Environment Variables

Backend `.env` is already configured with:
- Groq API Key
- Supabase credentials
- JWT settings

## 🎯 Next Steps

1. Open http://localhost:5173
2. Register a new account
3. Explore all features!

---
Built with ❤️ for mental wellness
