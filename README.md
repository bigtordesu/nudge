# Nudge — an ADHD-friendly day planner

A calm, shame-free planner for ADHD brains. It shows **one thing at a time**, makes time visible, breaks scary tasks into tiny steps, and helps when you're stuck. No account, no streaks, no guilt.

**Open it:** https://bigtordesu.github.io/nudge/

## Put it on your phone

- **iPhone:** open the link in **Safari** → tap **Share** (on newer iPhones it's under **•••**) → **Add to Home Screen** → **Add**.
- **Android:** open the link in **Chrome** → menu **⋮** → **Install app** / **Add to Home screen**.

It then opens full-screen like a normal app and works offline.

## What's inside

| Feature | What it does | Why (research) |
|---|---|---|
| **Right now** card | Shows a single next task with its next tiny step, a big Start button, "Not now" and "Pick for me" | ADHD is a problem of *doing* what you know at the right moment, so help works best at the point of action (Barkley) |
| **Energy check-in** | Low / Okay / High; Nudge picks tasks that fit your energy | Matches tasks to the brain you have today |
| **Day bar** | Hours left in your day, planned work drawn on it, and a reality check (with a +50% "ADHD buffer") | Time-perception problems are a core part of adult ADHD (Weissenberger et al., 2021) |
| **Focus timer** | A shrinking pie timer (5–60 min), brown / pink / white noise, time-check chimes and a little **focus buddy** | Visible time; white/pink noise gave a small attention boost in ADHD (Nigg et al., 2024 meta-analysis); body doubling |
| **Brain dump** | The big **+**: type everything in your head, one line per task, with automatic icons | Gets things out of working memory instantly |
| **Tiny steps** | "Break it down for me" writes first steps for common tasks (laundry, studying, emails, cleaning…) | Small concrete first actions beat vague tasks |
| **If-then plans** | "When ___, I will ___" for any task | If-then plans improved self-control in studies with children with ADHD (Gawrilow & Gollwitzer) |
| **Stuck? button** | Breathing minute, body check (water, food, meds, move), "shrink it", or "decide for me" (a slot-machine pick) | Overwhelm and decision paralysis |
| **Countdown** | "Dentist at 3pm": shows how long until you leave and which tasks fit before then | Beats "waiting mode" |
| **Routines** | Morning launch, Wind down, Leaving the house (+ templates); runs step by step with timers | Routines put decisions on autopilot |
| **Wins & dopamine menu** | A ta-da list, a weekly chart, "days you showed up" (never streaks), and a menu of healthy boosts | Shame fuels avoidance; quick rewards help ADHD motivation |
| **Wrap up the day** | Celebrate wins, move unfinished tasks to tomorrow or Later with no guilt, mood check, one thing for tomorrow | Ends the day on a good note (peak-end rule) |

The **Me → ADHD toolkit** section in the app explains each idea with its source.

## Privacy

Everything you add stays in your browser on your device. Nothing is sent anywhere. Use **Me → Settings → Back up** to save a copy (and **Restore** to load it on another phone).

Reminders and chimes play while the app is open; a web app can't send notifications when it's closed without a server.

## Sources

- Barkley on ADHD as a performance problem — [Simply Psychology](https://www.simplypsychology.org/adhd-future-blindness.html)
- Weissenberger et al. (2021), *Time perception is a focal symptom of ADHD in adults* — [PubMed](https://pubmed.ncbi.nlm.nih.gov/34272353/)
- Nigg et al. (2024), *Do white noise and pink noise help with attention in ADHD?* (13 studies, 335 participants) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11283987/)
- Gawrilow, Gollwitzer & Oettingen (2011), if-then plans and delay of gratification in ADHD — [PDF](https://www.socmot.uni-konstanz.de/sites/default/files/Gawrilow_Gollwitzer_Oettingen_Delay_2011-2.pdf)
- Body doubling for ADHD (2025) — [arXiv](https://arxiv.org/abs/2509.12153)
- Dopamine menus — [The Conversation](https://theconversation.com/dopamine-menus-the-science-behind-the-trend-and-how-it-might-help-people-with-adhd-218970)
- Shame and avoidance in ADHD — [USC Kortschak Center](https://kortschakcenter.usc.edu/wp-content/uploads/2026/04/Cognitive-Restructuring-for-ADHD_-Related-Shame-and-Procrastination.pdf)
- "Waiting mode" — [ADDitude](https://www.additudemag.com/adhd-time-blindness-waiting-mode/)
- Reviews of ADHD apps: [Frontiers in Public Health 2025](https://pubmed.ncbi.nlm.nih.gov/40084214), [JEHP 2025](https://journals.lww.com/jehp/fulltext/2025/12290/mobile_health__mhealth__apps_for_adhd__a.522.aspx)

Nudge is a support tool, not a treatment or medical advice.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app (HTML, CSS and JavaScript in one file) |
| `manifest.webmanifest` | Name, colours and icons for "Add to Home Screen" |
| `sw.js` | Service worker: offline support and updates |
| `icon-*.png` | App icons |
| `tools/make_icons.py` | Redraws the icons (`python tools/make_icons.py .`) |

To change something, edit `index.html` and push. The app picks up the new version the next time it's opened online.
