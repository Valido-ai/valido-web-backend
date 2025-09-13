# Valido Waitlist Backend 🚀

FastAPI backend for managing the waitlist of **users** (job seekers) and **organizations** (hirers).  
Stores data in **MongoDB** and sends email notifications when Valido goes live.  

---

## 🔹 Features
- Store **users** and **organizations** emails in separate collections.
- Prevent duplicate entries.
- Admin-only **launch notification** API to email everyone on the waitlist.
- Secure via **API key**.
- MongoDB powered.

---

### Clone Repo
```bash
git clone https://github.com/Valido-ai/valido-web-backend
cd valido-web-backend
