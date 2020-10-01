# Powell's Books Recommender

Book recommender system based on staff recommendations from Powell's Books.

## Summary

Powell's Books is an independent bookstore chain, based in Portland, Oregon. It was founded in 1971 and has 4 locations in the Portland Metro area. The company also operates a popular website at [Powells.com](https://www.powells.com).

A mainstay of Powell's are the staff picks. Picks are ubiquitous throughout the stores and popular with shoppers browsing for books. The card include a few handwritten sentences, often with drawings. Picks have also been added to Powell's website and organized by staff member.

This project includes several components to produce a recommender system.

- A SQLite database of staff recommendations, book/author details, reviews, and other info
- Scripts using Beautiful Soup 4 to scrape data from Powell's website
- Script to upload dataset to [Kaggle.com](https://www.kaggle.com)
- Jupyter notebooks with EDA and machine learning code
- Implementation of the recommender model using Streamlit

### Pictures of Powell's and Staff Picks

![Powell's Books marquee](./etc/img/powells-books-marquee.jpg)  
*Wikimedia Commons: Cacophony / [CC BY 3.0](https://creativecommons.org/licenses/by/3.0)*  
Powell's Books flagship bookstore at 1005 W Burnside St., Portland, OR 97209  

![Shelf with staff picks](./etc/img/shelf-staff-picks.jpg)  
*Wikimedia Commons: Another Believer / [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)*  
An example of Powell's staff picks

## The Dataset

### Staff Picks

Powell's website has a section of book recommendations organized by the staff members' first name and last initial. Each pick has a short blurb of why they are recommending the book.

### Staff Top Fives of the Year

At the end of each year, staff create members create a top five ranking of their recommended books. The top book has a short blurb on why the book is the top pick of the year.

## Database Schema

[Link to database schema](./db/powells_schema)

## License

This software is released under the MIT License. <https://opensource.org/licenses/MIT>

## References

- [Wikipedia: Powell's Books](https://en.wikipedia.org/wiki/Powell%27s_Books)
- [Powell's Books](https://www.powells.com/)
