# What is this?

MongoDB-like dot notation search in JSON (basically, reimplementation of "projection" in [find](https://docs.mongodb.com/manual/reference/method/db.collection.find/#db.collection.find))


## Progress

- [x] Python variant 1 (search each query data in source, upsert each pieace in result hashmap)
- [ ] Python variant 2 (optimize search pattern by grouping queries with same path levels, upsert in result hashmap)
- [ ] Python variant 3 (optimize search pattern by grouping queries with same path levels, pull just specific fields from hashmap in single iteration, ignore everything else)
- [ ] Java reflection variant 1
