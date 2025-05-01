# 📒 Address Book Search Project

This project implements a searchable address book API using different data structures and search algorithms. It's designed as a playground tool to observe the behavior and performance of various search strategies as data volume grows.

## 🔍 Implemented Search Algorithms

- **Linear Search** — Simple brute-force search
- **Binary Search** — Requires sorted data
- **Trie Search** — Efficient prefix matching

> Note.- Any new search algorithms must be registered in the `search_decorator.py`.

## 🧠 Search Algorithm Analysis

| Algorithm      | Worst Case Time Complexity | Description                                           |
|----------------|----------------------------|-------------------------------------------------------|
| Linear Search  | O(n)                       | Checks each item one by one until a the term is found |
| Binary Search  | O(log n)                   | Repeatedly divides a sorted list in half to search    |
| Trie Search    | O(m)                       | Traverses a character tree based on the input string  |

## 🌐 API Usage

The project exposes the following endpoints:

### GET `/search`

### Query Parameters

| Parameter      | Type   | Required | Description                                   |
|----------------|--------|----------|-----------------------------------------------|
| `name`         | string | No       | Full name to search for                       |
| `phone_number` | string | No       | Full name to search for                       |
| `address`      | string | No       | Full or partial name to search for            |
| `search_type`  | int    | Yes      | Type of search: `Linear`, `Binary`, or `Trie` |

**Example:**

```bash
curl --location 'http://{server}:{port}/search?name=Allen%20%20Rick&search_type=Linear'
```

### Response Example

```json
[
    {
        "address": "123 CHOB,Georgia 12th District",
        "name": "Allen  Rick",
        "phone_number": "123-456-7890"
    }
]
```

## 📚 Data Reference

The dataset used in this project was extracted from Kaggle:

**Phone Book Dataset**  
URL: [https://www.kaggle.com/datasets/vidyaargade/phonebookdataset](https://www.kaggle.com/datasets/vidyaargade/phonebookdataset)  
Author: [Vidya Argade](https://www.kaggle.com/vidyaargade)
