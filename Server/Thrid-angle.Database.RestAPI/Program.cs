using Thrid_angle.Database.RestAPI.Mehtods;
using Thrid_angle.Database.RestAPI.DTO;

MethodsEntityFrameworcSQLite SQLite = new MethodsEntityFrameworcSQLite();

BookCard book =  new BookCard();
book.NameBook = "тест";
book.DateCreationBook = DateTime.Now;
SQLite.CreateDatabaseSQLite(book);