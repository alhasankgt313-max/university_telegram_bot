from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ضع هنا التوكن الذي حصلت عليه من BotFather
TOKEN = "1234567890:ABCDEFabcdef1234567890abcdef"

# أمر البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا 👋 أنا بوت المساعدة الجامعية!\n"
        "أستطيع مساعدتك في معرفة تفاصيل الجامعات، الجداول، والأسئلة العامة.\n"
        "استخدم /help لمعرفة الأوامر المتاحة."
    )

# أمر المساعدة
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 الأوامر المتاحة:\n"
        "/universities - عرض قائمة الجامعات\n"
        "/faculty <اسم الجامعة> - عرض الكليات التابعة لجامعة معينة\n"
        "/schedule <اسم الكلية> - عرض جدول المحاضرات أو الامتحانات\n"
        "/ask <سؤالك> - لطرح استفسار عام\n"
        "/contact - معلومات التواصل مع إدارة البوت\n"
        "/news - عرض آخر الأخبار الجامعية\n"
        "/feedback - إرسال اقتراح أو شكوى\n"
    )

# عرض قائمة الجامعات
async def universities(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏛️ الجامعات المتاحة:\n"
        "- جامعة الملك سعود\n"
        "- جامعة القاهرة\n"
        "- الجامعة الأردنية\n"
        "- جامعة بيروت العربية"
    )

# عرض الكليات
async def faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("يرجى كتابة اسم الجامعة بعد الأمر، مثل:\n/faculty جامعة القاهرة")
        return

    university = " ".join(context.args)
    faculties = {
        "جامعة الملك سعود": ["علوم الحاسب", "الهندسة", "الطب", "العلوم"],
        "جامعة القاهرة": ["الحقوق", "التجارة", "الآداب", "الهندسة"],
        "الجامعة الأردنية": ["العلوم التربوية", "الطب", "اللغات", "الاقتصاد"],
        "جامعة بيروت العربية": ["الحقوق", "الهندسة المعمارية", "إدارة الأعمال"],
    }

    if university in faculties:
        text = f"🎓 الكليات في {university}:\n" + "\n".join(faculties[university])
    else:
        text = f"لم أجد معلومات عن {university}."

    await update.message.reply_text(text)

# أمر الجدول
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("يرجى كتابة اسم الكلية بعد الأمر، مثل:\n/schedule الهندسة")
        return

    faculty = " ".join(context.args)
    await update.message.reply_text(f"🗓️ جدول {faculty}:\n- الأحد: رياضيات\n- الإثنين: فيزياء\n- الثلاثاء: برمجة\n- الأربعاء: مشروع\n- الخميس: مختبر")

# أمر طرح سؤال
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("يرجى كتابة سؤالك بعد الأمر، مثل:\n/ask متى يبدأ الفصل الدراسي؟")
        return

    question = " ".join(context.args)
    await update.message.reply_text(f"تم استلام سؤالك:\n❓ {question}\nسيتم الرد عليك قريبًا بإذن الله.")

# أمر التواصل
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 للتواصل مع إدارة البوت:\n"
        "البريد: support@unibot.com\n"
        "تيليجرام: @AdminUniBot"
    )

# أمر الأخبار
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 آخر الأخبار:\n"
        "- بدء التسجيل للفصل الثاني.\n"
        "- إعلان نتائج القبول في جامعة الملك سعود.\n"
        "- منح دراسية جديدة في جامعة القاهرة."
    )

# أمر الاقتراحات
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✍️ أرسل اقتراحك أو شكواك هنا، وسيتم مراجعتها من قبل الإدارة.")

# تشغيل التطبيق
app = ApplicationBuilder().token(TOKEN).build()

# إضافة الأوامر
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("universities", universities))
app.add_handler(CommandHandler("faculty", faculty))
app.add_handler(CommandHandler("schedule", schedule))
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("feedback", feedback))

# تشغيل البوت
print("🚀 البوت يعمل الآن...")
app.run_polling()
