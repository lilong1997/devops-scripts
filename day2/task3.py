# task3
skills = set()
skills.add('linux')
skills.add('k8s')
skills.add('python')
skills.add('k8s') # 不会重复 因为集合的元素具有唯一性
skills.remove('linux')
skills.discard('nonexistent')
print(skills)