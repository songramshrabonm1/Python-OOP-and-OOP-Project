# # https://docs.python.org/3/tutorial/classes.html read this 
# Python Official Documentation: Classes একটি বিশদ ব্যাখ্যা প্রদান করে কীভাবে Python-এ ক্লাস তৈরি এবং ব্যবহার করা যায়। এটি ক্লাসের মূল উপাদান থেকে শুরু করে ইনহেরিটেন্স, প্রাইভেট ভ্যারিয়েবল, এবং আরও অনেক বিষয় কভার করে। আমি এখানে সেই ডকুমেন্টেশনের মূল বিষয়গুলো বাংলায় ব্যাখ্যা করবো।

# ক্লাস সম্পর্কে ধারণা
# ক্লাস হলো একটি ব্লুপ্রিন্ট বা কাঠামো যা থেকে অবজেক্ট তৈরি হয়। এটি ডেটা (ভ্যারিয়েবল) এবং ফাংশন (মেথড) ধারণ করতে পারে, যা ঐ ক্লাসের অন্তর্ভুক্ত অবজেক্টের উপর কাজ করে।

# ১. ক্লাস ডিফাইন করা
# Python-এ ক্লাস ডিফাইন করতে class কীওয়ার্ড ব্যবহার করা হয়।

# python
# Copy code
# class MyClass:
#     x = 5
# উপরের উদাহরণে, MyClass নামের একটি ক্লাস তৈরি করা হয়েছে যার মধ্যে একটি ভ্যারিয়েবল x রয়েছে।

# ২. অবজেক্ট তৈরি করা
# ক্লাস থেকে অবজেক্ট তৈরি করতে, আপনাকে ক্লাসের নাম দিয়ে সেটি ইনস্ট্যান্সিয়েট করতে হবে।

# python
# Copy code
# p1 = MyClass()
# print(p1.x)  # আউটপুট হবে: 5
# মেথড বা ফাংশন তৈরি করা
# ক্লাসের মধ্যে আপনি বিভিন্ন ফাংশন (মেথড) তৈরি করতে পারেন, যা ক্লাসের অবজেক্টের উপর কার্য সম্পাদন করে। মেথডগুলোর প্রথম প্যারামিটার হিসেবে self ব্যবহার করতে হয়, যা ওই অবজেক্টকে নির্দেশ করে যেটির উপর মেথডটি কাজ করবে।

# python
# Copy code
# class MyClass:
#     def say_hello(self):
#         print("Hello!")
        
# p1 = MyClass()
# p1.say_hello()  # আউটপুট: Hello!
# __init__() মেথড (Constructor)
# __init__() হল একটি বিশেষ মেথড, যা কনস্ট্রাক্টর নামে পরিচিত। যখন একটি নতুন অবজেক্ট তৈরি হয়, তখন এটি স্বয়ংক্রিয়ভাবে কল হয় এবং অবজেক্টের প্রাথমিক মানগুলো সেট করার জন্য ব্যবহৃত হয়।

# python
# Copy code
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)
# print(p1.name)  # আউটপুট: John
# এখানে, Person ক্লাসের একটি নতুন অবজেক্ট তৈরি করা হলে __init__() মেথডটি কল হয় এবং নাম ও বয়স সেট করা হয়।

# self কী?
# self হলো সেই অবজেক্টের রেফারেন্স যার সাথে মেথডটি কাজ করছে। আপনি যখন কোনো মেথডে self ব্যবহার করেন, তখন সেই মেথডটি ওই অবজেক্টের ভ্যারিয়েবল বা অন্যান্য মেথডের সাথে কাজ করতে পারে।

# python
# Copy code
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# p1 = Person("Alice")
# p1.greet()  # আউটপুট: Hello, my name is Alice
# ক্লাস ভ্যারিয়েবল এবং ইনস্ট্যান্স ভ্যারিয়েবল
# ক্লাস ভ্যারিয়েবল: এটি ক্লাসের সকল অবজেক্টের জন্য একই থাকে।
# ইনস্ট্যান্স ভ্যারিয়েবল: প্রতিটি অবজেক্টের জন্য আলাদা মান থাকে।
# python
# Copy code
# class Dog:
#     species = "Canine"  # ক্লাস ভ্যারিয়েবল

#     def __init__(self, name):
#         self.name = name  # ইনস্ট্যান্স ভ্যারিয়েবল

# dog1 = Dog("Buddy")
# dog2 = Dog("Max")

# print(dog1.species)  # আউটপুট: Canine
# print(dog1.name)     # আউটপুট: Buddy
# ইনহেরিটেন্স (Inheritance)
# ইনহেরিটেন্স এর মাধ্যমে একটি নতুন ক্লাস অন্য একটি বিদ্যমান ক্লাসের সব ফিচার উত্তরাধিকার সূত্রে পায়। অর্থাৎ, আপনি একটি ক্লাস থেকে আরেকটি ক্লাস তৈরি করে তার মেথড এবং প্রোপার্টি ব্যবহার করতে পারেন।

# python
# Copy code
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} is making a noise")

# class Dog(Animal):  # Dog ক্লাসটি Animal ক্লাস থেকে ইনহেরিট করেছে
#     def speak(self):
#         print(f"{self.name} is barking")

# dog = Dog("Buddy")
# dog.speak()  # আউটপুট: Buddy is barking
# উপরের উদাহরণে, Dog ক্লাসটি Animal ক্লাস থেকে ইনহেরিট করেছে এবং speak() মেথডটি ওভাররাইড করেছে।

# প্রাইভেট ভ্যারিয়েবল এবং মেথড
# Python-এ ভ্যারিয়েবলকে প্রাইভেট করতে তার আগে ডাবল আন্ডারস্কোর (__) ব্যবহার করা হয়। প্রাইভেট ভ্যারিয়েবল এবং মেথড ক্লাসের বাইরে থেকে অ্যাক্সেস করা যায় না।

# python
# Copy code
# class MyClass:
#     def __init__(self):
#         self.__private_var = 10  # প্রাইভেট ভ্যারিয়েবল

#     def __private_method(self):
#         print("This is a private method")

# obj = MyClass()
# # obj.__private_var  # AttributeError হবে
# মাল্টিপল ইনহেরিটেন্স
# Python-এ একাধিক ক্লাস থেকে ইনহেরিট করা সম্ভব। একে মাল্টিপল ইনহেরিটেন্স বলা হয়।

# python
# Copy code
# class A:
#     def method_a(self):
#         print("A")

# class B:
#     def method_b(self):
#         print("B")

# class C(A, B):
#     pass

# obj = C()
# obj.method_a()  # আউটপুট: A
# obj.method_b()  # আউটপুট: B
# মেথড ওভাররাইডিং
# মেথড ওভাররাইডিং হচ্ছে যখন একটি সাব-ক্লাস তার প্যারেন্ট ক্লাসের মেথড পুনরায় সংজ্ঞায়িত করে।

# python
# Copy code
# class Animal:
#     def speak(self):
#         print("Animal is making a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog is barking")

# dog = Dog()
# dog.speak()  # আউটপুট: Dog is barking
# মেথড রেজোলিউশন অর্ডার (MRO)
# Python-এ যখন একটি সাব-ক্লাস একাধিক ক্লাস থেকে ইনহেরিট করে, তখন মেথড রেজোলিউশন অর্ডার (MRO) ঠিক করে কোন মেথডটি আগে কল হবে। এটি সাধারণত ডেপথ-ফার্স্ট, লেফট-টু-রাইট অর্ডারে কাজ করে।

# ক্লাস ও অবজেক্টের উপসংহার
# ক্লাস হলো অবজেক্ট তৈরির একটি খাঁকা।
# অবজেক্ট হলো ক্লাসের একটি উদাহরণ, যা ক্লাসের ভ্যারিয়েবল ও মেথড ব্যবহার করে।
# Python-এ ইনহেরিটেন্স, পলিমরফিজম, এবং এনক্যাপসুলেশন মতো বৈশিষ্ট্যগুলো ক্লাস ব্যবহারের মাধ্যমে অর্জন করা যায়।
# এই ছিল Python-এর ক্লাস সম্পর্কে বাংলায় একটি সংক্ষিপ্ত ব্যাখ্যা।