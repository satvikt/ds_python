def split_list(lst, chunks):
    #print(lst)
    #print()
    chunks_yielded = 0
    total_sum = sum(lst)
    avg_sum = total_sum/float(chunks)
    chunk = []
    chunksum = 0
    sum_of_seen = 0

    for i, item in enumerate(lst):
        #print('start of loop! chunk: {}, index: {}, item: {}, chunksum: {}'.format(chunk, i, item, chunksum))
        if chunks - chunks_yielded == 1:
            #print('must yield the rest of the list! chunks_yielded: {}'.format(chunks_yielded))
            yield chunk + lst[i:]
            raise StopIteration

        to_yield = chunks - chunks_yielded
        chunks_left = len(lst) - i
        if to_yield > chunks_left:
            #print('must yield remaining list in single item chunks! to_yield: {}, chunks_left: {}'.format(to_yield, chunks_left))
            if chunk:
                yield chunk
            yield from ([x] for x in lst[i:])
            raise StopIteration

        sum_of_seen += item
        if chunksum < avg_sum:
            #print('appending {} to chunk {}'.format(item, chunk))
            chunk.append(item)
            chunksum += item
        else:
            #print('yielding chunk {}'.format(chunk))
            yield chunk
            # update average expected sum, because the last yielded chunk was probably not perfect:
            avg_sum = (total_sum - sum_of_seen)/(to_yield - 1)
            chunks_yielded += 1
            chunksum = item
            chunk = [item]

if __name__ == "__main__":
    import random
    lst = [1, 6, 2, 3, 4, 1, 7, 6, 4]
    #lst = [random.choice(range(1,101)) for _ in range(100)]
    chunks = 3
    print('list: {}, avg sum: {}, chunks: {}\n'.format(lst, sum(lst)/float(chunks), chunks))
    for chunk in split_list(lst, chunks):
        print('chunk: {}, sum: {}'.format(chunk, sum(chunk)))
