import matplotlib.pyplot as plt
from collections import Counter

category_correct = {}
category_correct_count = {}
# Show categories in a group chart
def show_groupchart(questions, category_correct):
    chart_category_count = Counter(question['category'][0] for question in questions)
    category_correct_count = Counter(category_correct)
    categories = list(chart_category_count.keys())
    total_questions = list(chart_category_count.values())
    correct_questions = [category_correct_count.get(cat, 0) for cat in categories]

    fig, ax = plt.subplots()
    index = range(len(categories))
    bar_width = 0.35

    rects1 = ax.bar(index, total_questions, bar_width, label='Total Questions')
    rects2 = ax.bar([i + bar_width for i in index], correct_questions, bar_width, label='Correct Questions')

    ax.set_xlabel('Categories')
    ax.set_ylabel('Frequency')
    ax.set_title('Total vs Correct Questions by Category')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(categories)
    ax.legend()

    plt.show()
