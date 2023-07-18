using Thrid_angle.Database.RestAPI.Mehtods;
using Thrid_angle.Database.RestAPI.DTO;
using System.Collections.Generic;

MethodsEntityFrameworcSQLite SQLite = new MethodsEntityFrameworcSQLite();

BookCard book =  new BookCard();
book.NameBook = "тест";
book.DateCreationBook = DateTime.Now;
book.AuthorBook = "Автор";
book.DescriptionBook = "Description";
book.DateUpdateBook = DateTime.Now;
book.PhotoBook = 123;
book.PriceBook = 0;
book.VendorCodeBook = "VendorCodeBook";
book.RecieptDateBook = DateTime.Now;
book.GenreBook = "Тест";


 SQLite.CreateDatabaseBookCard(book);
 //SQLite.UpdateDatabaseBookCard(book);



//List<BookCard> r = SQLite.ReadDatabaseBookCard();
//
//foreach (BookCard card in r)
//{
//    Console.WriteLine($" IdBook - {card.IdBook} NameBook -  {card.NameBook}  DateUpdateBook - {card.DateUpdateBook} AuthorBook - {card.AuthorBook}"  );
//      }