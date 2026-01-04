def solution(todo_list, finished):
    result = []

    for todo, done in zip(todo_list, finished):
        if not done:
            result.append(todo)

    return result
