using Thrid_angle.Database.RestAPI.Mehtods;
using Thrid_angle.Database.RestAPI.DTO;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc.Routing;
using System.Text.Json;

MethodsEntityFrameworcSQLite SQLite = new MethodsEntityFrameworcSQLite();

BookCard book = new BookCard();


book.NameBook = "тест";
book.DateCreationBook = DateTime.Now;
book.AuthorBook = "Автор";
book.DescriptionBook = "Description";
book.DateUpdateBook = DateTime.Now;
book.PhotoBook = 123;
book.PriceBook = 1;
book.VendorCodeBook = "VendorCodeBook";
book.RecieptDateBook = DateTime.Now;
book.GenreBook = "Тест";

 //WriteIndented = true,
var options = new JsonSerializerOptions { AllowTrailingCommas = false, PropertyNameCaseInsensitive = true,   NumberHandling = System.Text.Json.Serialization.JsonNumberHandling.AllowReadingFromString, WriteIndented = true, IncludeFields =true, };

string json1 = JsonSerializer.Serialize<BookCard>(book, options);

//BookCard book1 = JsonSerializer.Deserialize<BookCard>(json1);



Console.WriteLine(json1);




// SQLite.CreateDatabaseBookCard(book);
//SQLite.UpdateDatabaseBookCard(book);



//List<BookCard> r = SQLite.ReadDatabaseBookCard();
//
//foreach (BookCard card in r)
//{
//    Console.WriteLine($" IdBook - {card.IdBook} NameBook -  {card.NameBook}  DateUpdateBook - {card.DateUpdateBook} AuthorBook - {card.AuthorBook}"  );
//      }