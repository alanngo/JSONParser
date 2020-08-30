# Working w/ JSON files
- JSON supports 6 main types
    1. string
    2. number
    3. boolean
    4. null
    5. object
    6. array
- Formatting: <b>"Key":<i>[VALUE]</i></b>
    - [VALUE] can be any of the 6 types listed above
    - keys MUST BE strings
```json5
[
    { // JSON Object
      "ID": 0,
      "Name": "Varshika",
      "Language": "c++",
      "LovesShell": false,
      "Hobbies": ["sleeping", "programming", "watching tv"]
    },
    {// JSON Object
      "ID": 1,
      "Name": "Omar",
      "Language": "java",
      "LovesShell": true,
      "Hobbies": ["learning SQL", "buying macbooks"]
    },
    {// JSON Object
      "ID": 2,
      "Name": "Kevin",
      "Language": "javascript",
      "LovesShell": true,
      "Hobbies": ["skateboarding", "coding", "sleeping", "hanging out"]
    },
    {// JSON Object
      "ID": 3,
      "Name": "Smruti",
      "Language": "python",
      "LovesShell": false,
      "Hobbies": ["bubble tea", "sleeping", "front-end dev"]
    }
]
```