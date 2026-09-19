scores = [85, 92, 76, 88, 95]

average = sum(scores) / len(scores)
highest = max(scores)
passed = [score for score in scores if score >= 60]

print(f"平均分：{average:.1f}")
print(f"最高分：{highest}")
print(f"及格人数：{len(passed)} / {len(scores)}")