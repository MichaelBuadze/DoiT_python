# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს 
# სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები.

# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ.

# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით.

# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით.


import requests
import statistics
# import textwrap ვაპირებდი გრძელი ტექსტების გადატანას, მაგრამ რაღაც ბოლომდე ვერ ვქენი. 

# 1. მოთხოვნა "https://fakestoreapi.com/products" API-ზე
response = requests.get("https://fakestoreapi.com/products")

# 2. სტატუსის შემოწმება

# ონლაინ ძიების შედეგად მოპოვებული ინფო:
#   200: წარმატებული მოთხოვნა. სერვერმა დააბრუნა წარმატებული პასუხი.
#   404: სერვერი ვერ პოულობს მოთხოვნილ რესურსს (Not Found).
#   500: სერვერის შიდა შეცდომა (Internal Server Error).

if response.status_code == 200:

    # მიღებული მონაცემების გადაყვანა JSON ფორმატში, ანუ პითონის ლისტად
    products = response.json()

    # ა) პროდუქტის ფასების სია
    prices = [product['price'] for product in products] 
    # იქმნება ფასების ახალი სია -(list), სადაც შემდეგი ფორმულა ეძებს მაქსიმუმ, მინიმუმს და საშუალოს

    max_price = max(prices)  # მაქსიმალური ფასი
    min_price = min(prices)  # მინიმალური ფასი
    avg_price = statistics.mean(prices)  # საშუალო ფასის მარტივი გამოსავალი ნაპოვნია :) 

    print("\n" + "=" * 25)
    print(f"  Max Price: {max_price}")
    print("-" * 25)
    print(f"  Min Price: {min_price}")
    print("-" * 25)
    print(f"  Average Price: {avg_price}")
    print("=" * 25)
    print("=" * 110)

    # ბ) კატეგორიების სორტირებული სია (დუბლიკაციების გარეშე)
    categories = sorted(set(product['category'] for product in products))
    print("  Categories:", categories)

    # გ) პროდუქტის აღწერა (title) და id, დასორტირებული title-ის მიხედვით
    title_id_list = sorted([(product['title'], product['id']) for product in products], key=lambda x: x[0])
    print("=" * 110)
    print("  Title and ID list sorted by Title:")
    print("-" * 110)
    print("  Title:" + " " * 94 + "ID:")
    print("=" * 110)
    for title, prod_id in title_id_list:
        print(f"  {title:<100}{prod_id}")
        print("-" * 110)

    # დ) რეიტინგების სია, სორტირებული rate-ის მიხედვით ზრდადობით
    ratings_sorted = sorted([{'title': product['title'], 'rate': product['rating']['rate']} for product in products], key=lambda x: x['rate'])
    print("=" * 110)
    print("  Products sorted by rating:")
    print("-" * 110)
    print("  Title:" + " " * 94 + "Rating:")
    print("=" * 110)
    for item in ratings_sorted:
        
        print(f"  {item['title']:<100}{item['rate']}")
        # print(f"  {textwrap.fill(item['title'], width=65):<75}{item['rate']}") 
        # ვეცადე, მაგრამ რაღაცას ვაკლებ, კარგი იქნება თუ განვიხილავთ ლექციაზე. 
        print("-" * 110)
else:
    print(f"რაღაც არ წავიდა გეგმის მიხედვით, სტატუსის კოდი: {response.status_code}")
