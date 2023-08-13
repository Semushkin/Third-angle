using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Thrid_angle.Database.RestAPI.DTO;
using Thrid_angle.Database.RestAPI.Mehtods;

namespace Thrid_angle.Database.RestAPI.ControllersREST
{
    internal interface IControllers
    {

        
        public void CreateDatabaseBaskets( Guid IdUser, Guid IdBook,  int QuantityBooks,  int PricePerBook);
        public void CreateDatabaseBookCard(string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, string GenreBook, string DescriptionBook, decimal PriceBook);
        
        public void CreateDatabaseQuoteCard(string QuoteTitle, string QuoteText, string QuoteAutor);
        public void CreateDatabaseRequestCard(string CommentTextCard, int NumberStars, Guid IdUser, Guid IdBook);
        public void CreateDatabaseUserCard(string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser);


       
        public BookCard IDReadDatabaseBookCard(Guid IdBook);
     
        public QuoteCard IDReadDatabaseQuoteCard(Guid IdQuote);
        public RequestCard IDReadDatabaseRequestCard(Guid IdRequestCard);
        public UserCard IDReadDatabaseUserCard(Guid IdUser);


        public IEnumerable<Baskets>  UserReadDatabaseBaskets(Guid IdUser);
        public IEnumerable<BookCard> ReadDatabaseBookCard();
        public IEnumerable<Baskets> UserReadDatabaseOrderCard(Guid IdUser);
        public IEnumerable<RequestCard> IdUserReadDatabaseRequestCard(Guid IdUser);
        public IEnumerable<RequestCard> IdBookReadDatabaseRequestCard(Guid IdBook);
        public IEnumerable<UserCard> LoginUserReadDatabaseUserCard(string LoginUser, string PasswordUser);


        public void UpdateDatabaseBaskets(Guid IdBasket, int QuantityBooks, int PricePerBook);
        public void UpdateDatabaseBookCard(Guid IdBook, string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, string GenreBook, string DescriptionBook, decimal PriceBook);
        public void UpdateDatabaseOrderCard( Guid NumberOrderCard, string StatusOrderCard);
        public void UpdateDatabaseQuoteCard(Guid IdQuote, string QuoteTitle, string QuoteText, string QuoteAutor);
        public void UpdateDatabaseRequestCard(Guid IdRequestCard, string CommentTextCard, int NumberStars);
        public void UpdateDatabaseUserCard(Guid IdUser, string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser);



        public void DeleteDatabaseBaskets(Guid IdBasket);
        public void DeleteDatabaseBookCard(Guid IdBook);
        public void DeleteDatabaseOrderCard(Guid IdOrder);
        public void DeleteDatabaseQuoteCard(Guid IdQuote);
        public void DeleteDatabaseRequestCard(Guid IdRequestCard);
        public void DeleteDatabaseUserCard(Guid IdUser);
        public void CreateDatabaseBasketsStatusOrderCard(Guid IdUser);






    }
}
