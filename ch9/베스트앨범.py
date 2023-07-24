#1.
# 장르별로 딕셔너리를 만들고 재생횟수 합한다
# 장르 안에 재생횟수로 정렬
# 앞에서 두개 리턴

## 서로 다른 정렬 기준을 가지고 싶다면 reverse가 아니라 -를 붙여서 정렬하면 된다.

def solution(genres, plays):
    answer = []

    genres_plays_count_dict = {}
    genres_plays_list_dict = {}

    for g, p in zip(genres, plays):
        if genres_plays_count_dict.get(g):
            genres_plays_count_dict[g] += p
        else:
            genres_plays_count_dict[g] = p

    for i, v in enumerate(zip(genres, plays)):
        g = v[0]
        p = v[1]
        if genres_plays_list_dict.get(g):
            genres_plays_list_dict[g].append((i, p))
        else:
            genres_plays_list_dict[g] = [(i, p)]

    for g in genres_plays_list_dict:
        genres_plays_list_dict[g].sort(key=lambda x: (-x[1], x[0]))

    genres_plays_count_sort = sorted(genres_plays_count_dict.items(), key=lambda x: x[1], reverse=True)

    for g, p in genres_plays_count_sort:
        for i, p in genres_plays_list_dict[g][:2]:
            answer.append(i)

    return answer