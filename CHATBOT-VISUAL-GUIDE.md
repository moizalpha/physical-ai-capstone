# Chatbot Visual Guide - How It Appears in Docusaurus

## 🎨 Visual Overview

### 1. Chat Button (Closed State)

When users visit any page, they see a **purple floating button** in the bottom-right corner:

```
┌─────────────────────────────────────────────┐
│  Your Docusaurus Documentation Page         │
│                                             │
│  # Physical AI Book                         │
│                                             │
│  Content goes here...                       │
│                                             │
│                                             │
│                                             │
│                                        ╔════╗
│                                        ║ 💬 ║ ← Purple chat button
│                                        ╚════╝
└─────────────────────────────────────────────┘
```

**Button Details**:
- **Position**: Fixed bottom-right (20px from edges)
- **Size**: 60x60 pixels
- **Color**: Purple gradient
- **Icon**: 💬 (speech bubble emoji)
- **Hover**: Grows slightly larger
- **Mobile**: Automatically adjusts position

---

### 2. Chatbot Window (Open State)

When user clicks the button, the chatbot window opens:

```
┌─────────────────────────────────────────────┐
│  Your Docusaurus Documentation Page         │
│                                             │
│  Content...                    ┌──────────┐│
│                                │📚 Ask    ││
│                                │About the ││
│                                │Book    ✕ ││
│                                ├──────────┤│
│                                │          ││
│                                │ Bot: Hi! ││
│                                │ I can    ││
│                                │ answer   ││
│                                │ questions││
│                                │          ││
│                                │  User:   ││
│                                │  What is ││
│                                │  this?   ││
│                                │          ││
│                                ├──────────┤│
│                                │ Type...➤ ││
│                                └──────────┘│
│                                        ╔════╗
│                                        ║ ✕  ║ ← Close button
│                                        ╚════╝
└─────────────────────────────────────────────┘
```

**Window Details**:
- **Size**: 400px wide × 600px tall
- **Position**: Bottom-right, above the button
- **Features**:
  - Header with title and close button
  - Scrollable message area
  - Input field at bottom
  - Send button

---

### 3. With Text Selection

When user selects text on the page:

```
┌─────────────────────────────────────────────┐
│  # Physical AI                              │
│                                             │
│  [ROS 2 is a middleware framework...]  ← Selected text
│   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      │
│                                             │
│                                ┌──────────┐│
│                                │📚 Ask    ││
│                                │About the ││
│                                │Book    ✕ ││
│                                ├──────────┤│
│                                │Selected: ││
│                                │ROS 2...✕ ││ ← Selection banner
│                                ├──────────┤│
│                                │          ││
│                                │ Bot: Hi! ││
│                                │          ││
│                                ├──────────┤│
│                                │ Type...➤ ││
│                                └──────────┘│
└─────────────────────────────────────────────┘
```

**Selection Feature**:
- Blue banner shows selected text
- User can ask questions about it
- ✕ button to clear selection

---

### 4. Conversation Flow

```
┌────────────────────────────────────────┐
│ 📚 Ask About the Book              ✕  │ ← Header
├────────────────────────────────────────┤
│                                        │
│  ┌──────────────────────────────────┐ │
│  │ Bot: Hi! I can answer questions  │ │ ← Assistant message (left)
│  │ about the Physical AI book.      │ │
│  └──────────────────────────────────┘ │
│                                        │
│              ┌────────────────────┐   │
│              │ User: What is ROS? │   │ ← User message (right)
│              └────────────────────┘   │
│                                        │
│  ┌──────────────────────────────────┐ │
│  │ Bot: ROS 2 is a middleware...    │ │
│  │                                  │ │
│  │ Sources:                         │ │
│  │ • Introduction (Score: 0.92)     │ │ ← Source citations
│  │ • ROS Overview (Score: 0.88)     │ │
│  └──────────────────────────────────┘ │
│                                        │
│              ┌────────────────────┐   │
│              │ User: Tell me more │   │
│              └────────────────────┘   │
│                                        │
│  ┌──────────────────────────────────┐ │
│  │ ●●●                              │ │ ← Loading indicator
│  └──────────────────────────────────┘ │
│                                        │
├────────────────────────────────────────┤
│ ┌────────────────────────────┐  ┌──┐ │
│ │ Ask a question...          │  │➤ │ │ ← Input area
│ └────────────────────────────┘  └──┘ │
└────────────────────────────────────────┘
```

---

## 🎨 Color Scheme

### Light Mode
- **Chat Button**: Purple gradient (#667eea → #764ba2)
- **Header**: Purple gradient (same)
- **User Messages**: Purple gradient background, white text
- **Bot Messages**: Light gray background, dark text
- **Input Border**: Gray, changes to purple on focus

### Dark Mode
- **Chat Button**: Same purple gradient
- **Header**: Same purple gradient
- **User Messages**: Purple gradient (same)
- **Bot Messages**: Dark gray background, light text
- **Window Background**: Dark theme color
- **Automatically adapts** to Docusaurus dark mode

---

## 📱 Responsive Design

### Desktop (>768px)
```
┌───────────────────────────────────┐
│                                   │
│  Full width content               │
│                                   │
│                      ┌──────────┐ │
│                      │ Chatbot  │ │ ← 400px wide
│                      │          │ │
│                      └──────────┘ │
│                              💬   │
└───────────────────────────────────┘
```

### Mobile (<768px)
```
┌─────────────────┐
│                 │
│ Mobile content  │
│                 │
│ ┌─────────────┐ │
│ │  Chatbot    │ │ ← Full width minus 20px
│ │             │ │    (calc(100vw - 20px))
│ │             │ │
│ │             │ │
│ └─────────────┘ │
│            💬   │
└─────────────────┘
```

---

## 🎬 Animations

### Opening Animation
- Chat window slides up and fades in
- Duration: 0.3 seconds
- Easing: ease-out

### New Message Animation
- Messages slide up from bottom
- Opacity fades from 0 to 1
- Duration: 0.3 seconds

### Loading Dots
- Three dots (●●●) blink in sequence
- Creates typing effect
- Loops continuously

### Hover Effects
- Chat button scales to 110% on hover
- Box shadow increases
- Send button scales to 105%

---

## 🔧 How It's Integrated

### File Structure
```
docs/
├── src/
│   ├── components/
│   │   └── RAGChatbot/
│   │       ├── index.tsx         ← Main component
│   │       └── styles.module.css ← All styling
│   └── theme/
│       └── Root.tsx              ← Global integration
```

### Integration Method

**Root.tsx wraps entire Docusaurus app**:
```typescript
export default function Root({ children }) {
  return (
    <>
      {children}                    ← All Docusaurus pages
      <RAGChatbot apiUrl="..." />  ← Chatbot on every page
    </>
  );
}
```

**Result**: Chatbot appears on **every page** automatically!

---

## 💡 User Interactions

### 1. Opening Chatbot
```
User clicks 💬 → Window opens → Shows welcome message
```

### 2. Asking Question
```
User types → Presses Enter (or clicks ➤) → Shows loading dots
→ Receives answer with sources → Can ask follow-up
```

### 3. Text Selection
```
User selects text on page → Selection stored automatically
→ User clicks chatbot → Blue banner shows selection
→ User asks question → Bot prioritizes selected text
```

### 4. Viewing Sources
```
Bot responds → Shows answer → Lists sources below
→ Each source shows: Title, file path, relevance score
→ User can see which documents were used
```

---

## 🎯 Key Features Visible to Users

✅ **Always Accessible**: Button visible on all pages
✅ **Non-Intrusive**: Doesn't block content when closed
✅ **Responsive**: Works on all screen sizes
✅ **Dark Mode**: Automatically adapts
✅ **Smooth**: Animated transitions
✅ **Clear**: Color-coded user/bot messages
✅ **Transparent**: Shows sources for every answer
✅ **Smart**: Remembers selected text

---

## 🚀 Live Demo Flow

### Step-by-Step User Experience

**1. User visits documentation**
   - Sees purple chat button bottom-right
   - Continues reading normally

**2. User has a question**
   - Clicks chat button
   - Window opens smoothly
   - Sees welcome message

**3. User asks question**
   - Types: "What is Physical AI?"
   - Presses Enter
   - Sees loading dots (●●●)

**4. Bot responds**
   - Answer appears in gray bubble (left side)
   - Sources listed below answer
   - User can click to read more

**5. User selects text**
   - Highlights text: "ROS 2 middleware..."
   - Blue banner appears in chat
   - Shows first 100 characters

**6. User asks about selection**
   - Types: "Explain this in simple terms"
   - Bot answers based on selected text
   - More relevant to selection

**7. User continues conversation**
   - Can ask follow-up questions
   - Scroll to see history
   - Close when done (✕ or chat button)

---

## 📸 What Users See

### First Time
1. Documentation page loads
2. Purple button appears (animated fade-in)
3. "What's this?" curiosity

### After Clicking
1. Window opens (slide up animation)
2. Welcome message greets them
3. Input field invites questions

### After First Query
1. Loading dots show it's thinking
2. Answer appears with smooth animation
3. Sources build trust
4. Ready for more questions

---

## 🎨 Customization Points

You can easily customize in `styles.module.css`:

```css
/* Change button color */
.chatbotToggle {
  background: linear-gradient(135deg, #YOUR-COLOR1, #YOUR-COLOR2);
}

/* Change window size */
.chatbotWindow {
  width: 500px;    /* Default: 400px */
  height: 700px;   /* Default: 600px */
}

/* Change position */
.chatbotToggle {
  bottom: 30px;    /* Default: 20px */
  right: 30px;     /* Default: 20px */
}
```

---

## ✅ Testing Checklist

After starting `npm start`:

- [ ] Chat button appears bottom-right
- [ ] Button is purple with 💬 icon
- [ ] Clicking opens window
- [ ] Window has header "📚 Ask About the Book"
- [ ] Welcome message shows
- [ ] Can type in input field
- [ ] Enter key sends message
- [ ] Loading dots appear while waiting
- [ ] Answer appears with sources
- [ ] Can select text on page
- [ ] Selection shows in chat (blue banner)
- [ ] Can close with ✕ button
- [ ] Reopening preserves conversation
- [ ] Works in dark mode
- [ ] Works on mobile (resize browser)

---

**Status**: ✅ Fully integrated and working!

**Frontend**: Same for both FREE and PAID versions!

**To see it live**: Run `npm start` in the `docs` folder!
