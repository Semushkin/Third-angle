
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc.Routing;
using System.Text.Json;
using Microsoft.Extensions.DependencyInjection;
using System;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.HttpLogging;

using Thrid_angle.Database.RestAPI.ControllersREST;
using Thrid_angle.Database.RestAPI.Database;
using Thrid_angle.Database.RestAPI.Mehtods;
using Thrid_angle.Database.RestAPI.DTO;
using Microsoft.AspNetCore.Builder;
using Thrid_angle.Database.RestAPI;
using System.Net.Http.Headers;





internal class Program
{
    private static void Main(string[] args)
    {


        var folder1 = Environment.SpecialFolder.LocalApplicationData;
        string path1 = Environment.GetFolderPath(folder1);

        Console.WriteLine("вот сюда нужно положить базу данных -  " + path1);
        

        var builder = WebApplication.CreateBuilder(args);


       
        builder.Services.AddSingleton<IControllers, ServicesRest>();
       
        builder.Services.AddControllers();


        builder.Services.AddControllersWithViews();

        //настройка http clienta
        builder.Services.AddHttpClient(name: "Northwind.WebApi",
         configureClient: options =>
         {
             options.BaseAddress = new Uri("https://localhost:5002/");

             options.DefaultRequestHeaders.Accept.Add(
             new MediaTypeWithQualityHeaderValue(
             "application/json", 1.0));
         });

        //настройка версии http
        builder.Services.AddHttpLogging(options =>
        {
            options.LoggingFields = HttpLoggingFields.All;
            options.RequestBodyLogLimit = 4096; // по умолчанию 32 Кбайт
            options.ResponseBodyLogLimit = 4096; // по умолчанию 32 Кбайт
        });



        builder.Services.AddDbContext<DatabaseContext>();
        builder.Services.AddWebEncoders();
        builder.Services.AddSwaggerGen();
        builder.Services.AddControllers();
        builder.Services.AddAuthorization();
        builder.Services.AddEndpointsApiExplorer();


        // настройка http client



        //var http = builder.Services.AddHttpClient("Thrid-angle", httpClient =>  httpClient.BaseAddress = new Uri("https://localhost:5000/ServicesRest/") );

        //<HttpServicesCreateDatabaseUserCard>

        var app = builder.Build();
        app.UseHttpsRedirection();
        app.UseAuthorization();
        app.MapControllers();
        app.UseSwagger();
        app.UseSwaggerUI();
        app.UseHttpsRedirection();
        app.UseHsts();



        app.UseStaticFiles();

        app.UseRouting();


        app.UseEndpoints(endpoints =>
        {

            endpoints.MapControllerRoute(
                name: "default",
                pattern: "{controller=ServicesRest}/{action=CreateDatabaseBaskets}/{IdUser}/{IdBook}/{QuantityBooks}/{PricePerBook}");


            endpoints.MapControllerRoute(
                name: "default",
                pattern: "{controller=ServicesRest}/{action=CreateDatabaseBookCard}/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{GenreBook}/{DescriptionBook}/{PriceBook}");



            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=CreateDatabaseQuoteCard}/{QuoteTitle}/{QuoteText}/{QuoteAutor}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=CreateDatabaseRequestCard}/{CommentTextCard}/{NumberStars}/{IdUser}/{IdBook}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=CreateDatabaseUserCard}/{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}");


           


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=IDReadDatabaseBookCard}/{IdBook}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=IDReadDatabaseOrderCard}/{IdOrder}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=IDReadDatabaseQuoteCard}/{IdQuote}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=IDReadDatabaseRequestCard}/{IdRequestCard}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=IDReadDatabaseUserCard}/{IdUser}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=UpdateDatabaseBaskets}/{IdBasket}/{QuantityBooks}/{PricePerBook}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=UpdateDatabaseBookCard}/{IdBook}/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{GenreBook}/{DescriptionBook}/{PriceBook}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=UpdateDatabaseOrderCard}/{IdOrder}/{OrderCardBooksList}/{StatusOrderCard}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=UpdateDatabaseQuoteCard}/{IdQuote}/{QuoteTitle}/{QuoteText}/{QuoteAutor}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=UpdateDatabaseRequestCard}/{IdRequestCard}/{CommentTextCard}/{NumberStars}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=UpdateDatabaseUserCard}/{IdUser}/{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=DeleteDatabaseBaskets}/{IdBasket}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=DeleteDatabaseBookCard}/{IdBook}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=DeleteDatabaseOrderCard}/{IdOrder}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=DeleteDatabaseQuoteCard}/{IdQuote}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=DeleteDatabaseRequestCard}/{IdRequestCard}");


            endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=ServicesRest}/{action=DeleteDatabaseUserCard}/{IdUser}");

            endpoints.MapControllerRoute(
              name: "default",
              pattern: "{controller=ServicesRest}/{action=LoginUserReadDatabaseUserCard}/{LoginUser}/{PasswordUser}");


            endpoints.MapControllerRoute(
              name: "default",
              pattern: "{controller=ServicesRest}/{action=UserReadDatabaseBaskets}/{IdUser}");

        endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=ServicesRest}/{action=ReadDatabaseBookCard}");

            endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=ServicesRest}/{action=UserReadDatabaseOrderCard}/{IdUser}");


            endpoints.MapControllerRoute(
      name: "default",
      pattern: "{controller=ServicesRest}/{action=IdUserReadDatabaseRequestCard}/{IdUser}");

            endpoints.MapControllerRoute(
      name: "default",
      pattern: "{controller=ServicesRest}/{action=IdBookReadDatabaseRequestCard}/{IdBook}");

            endpoints.MapControllerRoute(
           name: "default",
           pattern: "{controller=ServicesRest}/{action=CreateDatabaseBasketsStatusOrderCard}/{IdUser}");

           


        });

        app.Run();


        var folder = Environment.SpecialFolder.LocalApplicationData;
        string path = Environment.GetFolderPath(folder);

       
       


    }
}