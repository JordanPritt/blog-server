Frequently when working with computers you will find that you need to work with files. Whether it is for storing notes, recipes, school work, spreadsheets, or any other kind of data that the every day user needs to use and interact with. For those working with software it may come as second nature to make and use files with their applications. How can you do this though? Well in this post we'll look at how you can use Python to work with files!

So you might be wondering, what does *working with files* mean? To be more clear that is creating, reading from, writing to, and removing files. We will look into how Python makes it easy and efficient to handle basic input/output with files and empower your next software project to utilize these tools!

## How to Create a File

Let's start with making a file. Seems like a god place to begin no? So with Python you ge ta lot of tools at you disposal in the [standard library](https://docs.python.org/3/library/index.html) that ships with Python. *Fyi the standard library has a ton of great features in it that's worth taking the time to dig into*. Let's exam a simple application that creates a file:

```python
def create_file():
    file = open('example.txt', 'wt')
    file.close()

if __name__ == '_main__':
    create_file()
```

Above we can see a simple application with a single function that creates a file handler that creates *example.txt* and then closes the file.