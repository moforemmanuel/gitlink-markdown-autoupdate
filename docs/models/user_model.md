# user_model Module

## Class: `User_Model`

This class provides functionality for manipulating with users.

### Attributes

- `name`: User's name.
- `age`: User's age.

### Methods

### `__init__(self) -> None` [[view source](/src/models/user_model.py#L5-L7)]

Initializes an User_Model instance.

**Returns**:

- `None`

**Example:**

```python
user = User_Model('John Doe', 37)
```

**Notes:**

This is just a dummy project to implement a core functionality of documentation generator; automatic file referencing/linking.

### `get_name(self) -> str` [[view source](https://github.com/{}/SMSwithoutborders-BE/blob/27ad8d4ed81ef73581515c2b2b17274d0fbaca72/src/models/grants.py#L45-L89)]

Gets the user's names.

**Parameters:**

- `None`

**Returns:**

- `str`: User's greetings with name

**Raises:**

- `TypeError`: name parameter is not a string.

**Example:**

```python
user = User_Model('John Doe', 37)
print(user.get_name())
```

### `get_age(self) -> str` [[view source](https://github.com/smswithoutborders/SMSwithoutborders-BE/blob/27ad8d4ed81ef73581515c2b2b17274d0fbaca72/src/models/grants.py#L45-L89)]

Gets the user's age.

**Parameters:**

- `None`

**Returns:**

- `str`: User's greetings with age

**Raises:**

- `TypeError`: age parameter is not a number.

**Example:**

```python
user = User_Model('John Doe', 37)
print(user.get_age())
```
