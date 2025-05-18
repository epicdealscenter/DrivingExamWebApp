
import streamlit as st
import json
import os

st.set_page_config(page_title="امتحان القيادة", layout="centered")

st.title("🛑 امتحان القيادة الرسمي")
st.write("اختر الإجابة الصحيحة لكل سؤال ثم اضغط على زر الإرسال في الأسفل.")

# Load questions
with open("arabic_exam_questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

user_answers = {}
score = 0

with st.form("exam_form"):
    for idx, q in enumerate(questions):
        image_path = os.path.join("images", q["image"])
        if os.path.exists(image_path):
            st.image(image_path, width=400)
        else:
            st.warning(f"❗ الصورة غير موجودة: {q['image']}")
        st.markdown(f"**{idx + 1}. {q['question']}**")
        user_answers[idx] = st.radio(
            f"السؤال {idx + 1}", 
            q["options"], 
            key=f"q{idx}"
        )
        st.markdown("---")

    submitted = st.form_submit_button("📤 إرسال الإجابات")

if submitted:
    st.subheader("🔍 النتيجة")
    for idx, q in enumerate(questions):
        correct = q["answer"]
        user_answer = user_answers[idx]
        is_correct = correct == user_answer
        st.markdown(f"**سؤال {idx + 1}: {'✅ صحيح' if is_correct else '❌ خطأ'}**")
        if not is_correct:
            st.markdown(f"الإجابة الصحيحة: {correct}")
        st.markdown("---")
        if is_correct:
            score += 1

    st.success(f"✅ نتيجتك: {score} من {len(questions)}")
