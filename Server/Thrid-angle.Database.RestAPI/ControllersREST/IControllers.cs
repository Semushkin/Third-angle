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


        public void CreateDatabaseBaskets(Guid IdUser, Guid IdBook, int QuantityBooks, int PricePerBook, DateTime DateCreationBasket, DateTime DateUbdateBasket);
        public void CreateDatabaseBookCard(string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, DateTime RecieptDateBook, string GenreBook, string DescriptionBook, decimal PriceBook, DateTime DateCreationBook, DateTime DateUpdateBook);
        public void CreateDatabaseOrderCard(String OrderCardBooksList, DateTime DateCreationOrderCard, DateTime DateUpdateOrderCard, string StatusOrderCard, Guid IdUsers);
        public void CreateDatabaseQuoteCard(string QuoteTitle, string QuoteText, string QuoteAutor, DateTime DateCreationQuote, DateTime DateUpdateQuote);
        public void CreateDatabaseRequestCard(string CommentTextCard, int NumberStars, Guid IdUser, Guid IdBook, DateTime DateRequestCreation, DateTime DateRequestUpdation);
        public void CreateDatabaseUserCard(string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime DateCreationUser, DateTime UpdateDateUser);


        public Baskets IDReadDatabaseBaskets(Guid IdBasket);
        public BookCard IDReadDatabaseBookCard(Guid IdBook);
        public OrderCard IDReadDatabaseOrderCard(Guid IdOrder);
        public QuoteCard IDReadDatabaseQuoteCard(Guid IdQuote);
        public RequestCard IDReadDatabaseRequestCard(Guid IdRequestCard);
        public UserCard IDReadDatabaseUserCard(Guid IdUser);


        public void UpdateDatabaseBaskets(Guid IdBasket, int QuantityBooks, int PricePerBook, DateTime DateUbdateBasket);
        public void UpdateDatabaseBookCard(Guid IdBook, string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, DateTime RecieptDateBook, string GenreBook, string DescriptionBook, decimal PriceBook, DateTime DateUpdateBook);
        public void UpdateDatabaseOrderCard(Guid IdOrder, String OrderCardBooksList, DateTime DateUpdateOrderCard, string StatusOrderCard);
        public void UpdateDatabaseQuoteCard(Guid IdQuote, string QuoteTitle, string QuoteText, string QuoteAutor, DateTime DateUpdateQuote);
        public void UpdateDatabaseRequestCard(Guid IdRequestCard, string CommentTextCard, int NumberStars, DateTime DateRequestUpdation);
        public void UpdateDatabaseUserCard(Guid IdUser, string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime UpdateDateUser);



        public void DeleteDatabaseBaskets(Guid IdBasket);
        public void DeleteDatabaseBookCard(Guid IdBook);
        public void DeleteDatabaseOrderCard(Guid IdOrder);
        public void DeleteDatabaseQuoteCard(Guid IdQuote);
        public void DeleteDatabaseRequestCard(Guid IdRequestCard);
        public void DeleteDatabaseUserCard(Guid IdUser);
       






    }
}
