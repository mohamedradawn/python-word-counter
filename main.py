def analyze_text(file_path):
    try:
        # 1. قراءة النص من الملف الخارجي
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text:
            print("الملف فارغ!")
            return

        # 2. حساب عدد الكلمات
        word_count = len(text.split())

        # 3. حساب عدد الجمل
        sentences_count = text.count('.') + text.count('?') + text.count('!')

        # 4. تنظيف النص وحساب الكلمات الأكثر تكراراً
        punctuation = ".,!?;:-()\"“”@"
        clean_text = text.lower()
        for p in punctuation:
            clean_text = clean_text.replace(p, " ")
        
        words_list = clean_text.split()
        word_counts = {}
        for word in words_list:
            word_counts[word] = word_counts.get(word, 0) + 1

        # 5. ترتيب وجلب أول 10
        top_10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        # --- طباعة التقرير النهائي ---
        print("-" * 30)
        print(f"Analysis for: {file_path}")
        print("-" * 30)
        print(f"Total Words:     {word_count}")
        print(f"Total Sentences: {sentences_count}")
        print("\nTop 10 Most Frequent Words:")
        for word, count in top_10:
            print(f"- {word}: {count}")
        print("-" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

# تشغيل البرنامج
if __name__ == "__main__":
    analyze_text('data.txt')
