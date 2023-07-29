
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc.Routing;
using System.Text.Json;
using Microsoft.Extensions.DependencyInjection;
using System;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Configuration;

using Thrid_angle.Database.RestAPI.ControllersREST;
using Thrid_angle.Database.RestAPI.Database;
using Thrid_angle.Database.RestAPI.Mehtods;
using Thrid_angle.Database.RestAPI.DTO;
using Microsoft.AspNetCore.Builder;
using Thrid_angle.Database.RestAPI;

MethodsEntityFrameworcSQLite SQLite = new MethodsEntityFrameworcSQLite();

BookCard book = new BookCard();

book.IdBook =  new Guid();                     
book.NameBook = "тест56";
book.DateCreationBook = DateTime.Now;
book.AuthorBook = "Автор256";
book.DescriptionBook = "Description";
book.DateUpdateBook = DateTime.Now;
book.PhotoBook = 1243;
book.PriceBook = 1;
book.VendorCodeBook = "VendorCodeBook";
book.RecieptDateBook = DateTime.Now;
book.GenreBook = "Тест36";


Baskets baskets = new Baskets();
baskets.IdBasket = new Guid("CD6450A8-A613-487A-9113-19A1BEC3A85C");
//baskets.IdUser = new Guid();
//baskets.IdBook = new Guid();
baskets.QuantityBooks = 27772;
baskets.PricePerBook = 10;
//baskets.DateCreationBasket = DateTime.Now;
baskets.DateUbdateBasket = DateTime.Now;



//WriteIndented = true,
//var options = new JsonSerializerOptions { AllowTrailingCommas = false, PropertyNameCaseInsensitive = true,   NumberHandling = System.Text.Json.Serialization.JsonNumberHandling.AllowReadingFromString, WriteIndented = true, IncludeFields =true, };
//
//string json1 = JsonSerializer.Serialize<BookCard>(book, options);

//BookCard book1 = JsonSerializer.Deserialize<BookCard>(json1);





//SQLite.UpdateDatabaseBaskets(baskets);

//SQLite.CreateDatabaseBaskets(baskets);
// SQLite.DeleteDatabaseBookCard(book.IdBook);



//List<BookCard> r = SQLite.ReadDatabaseBookCard();
//
//foreach (BookCard card in r)
//{
//    Console.WriteLine($" IdBook - {card.IdBook} NameBook -  {card.NameBook}  DateUpdateBook - {card.DateUpdateBook} AuthorBook - {card.AuthorBook}"  );
//      





var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<IControllers, Controllers>();

//builder.Services.Configure<Baskets>();

builder.Services.AddControllersWithViews();

builder.Services.AddDbContext<DatabaseContext>();
builder.Services.AddControllersWithViews();
builder.Services.AddSwaggerGen();
builder.Services.AddControllers();
builder.Services.AddAuthorization();
builder.Services.AddEndpointsApiExplorer();

var app = builder.Build();
app.UseHttpsRedirection();
app.UseSwagger();
app.UseSwaggerUI();


app.MapControllers();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.UseEndpoints(endpoints =>
{
    endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Controllers}/{action=CreateDatabaseBaskets}/{IdUser}/{IdBook}/{QuantityBooks}/{PricePerBook}/{DateCreationBasket}/{DateUbdateBasket}");

    endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Controllers}/{action=CreateDatabaseBookCard}/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{RecieptDateBook}/{GenreBook}/{DescriptionBook}/{PriceBook}/{DateCreationBook}/{DateUpdateBook}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=CreateDatabaseOrderCard}/{OrderCardBooksList}/{DateCreationOrderCard}/{DateUpdateOrderCard}/{StatusOrderCard}/{IdUsers}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=CreateDatabaseQuoteCard}/{QuoteTitle}/{QuoteText}/{QuoteAutor}/{DateCreationQuote}/{DateUpdateQuote}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=CreateDatabaseRequestCard}/{CommentTextCard}/{NumberStars}/{IdUser}/{IdBook}/{DateRequestCreation}/{DateRequestUpdation}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=CreateDatabaseUserCar}/{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{DateCreationUser}/{UpdateDateUser}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=IDReadDatabaseBaskets}/{IdBasket}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=IDReadDatabaseBookCard}/{IdBook}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=IDReadDatabaseOrderCard}/{IdOrder}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=IDReadDatabaseQuoteCard}/{IdQuote}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=IDReadDatabaseRequestCard}/{IdRequestCard}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=IDReadDatabaseUserCard}/{IdUser}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=UpdateDatabaseBaskets}/{IdBasket}/{QuantityBooks}/{PricePerBook}/{DateUbdateBasket}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=UpdateDatabaseBookCard}/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{RecieptDateBook}/{GenreBook}/{DescriptionBook}/{PriceBook}/{DateUpdateBook}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=UpdateDatabaseOrderCard}/{IdOrder}/{OrderCardBooksList}/{DateUpdateOrderCard}/{StatusOrderCard}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=UpdateDatabaseQuoteCard}/{IdQuote}/{QuoteTitle}/{QuoteText}/{QuoteAutor}/{DateUpdateQuote}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=UpdateDatabaseRequestCard}/{IdRequestCard}/{CommentTextCard}/{NumberStars}/{DateRequestUpdation}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=UpdateDatabaseUserCard}/{IdUser}/{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{UpdateDateUser}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=DeleteDatabaseBaskets}/{IdBasket}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=DeleteDatabaseBookCard}/{IdBook}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=DeleteDatabaseOrderCard}/{IdOrder}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=DeleteDatabaseQuoteCard}/{IdQuote}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=DeleteDatabaseRequestCard}/{IdRequestCard}");

    endpoints.MapControllerRoute(
       name: "default",
       pattern: "{controller=Controllers}/{action=DeleteDatabaseUserCard}/{IdUser}");



});


