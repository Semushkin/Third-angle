using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Web.Mvc;
using Microsoft.AspNetCore.Mvc.Routing;
using Thrid_angle.Database.RestAPI.DTO;

namespace Thrid_angle.Database.RestAPI.Controllers
{
    [RoutePrefix("/Controllers/")]
    public class Controllers
    {
        [Route("CreateDatabaseBaskets/{IdUser}/{IdBook}/{QuantityBooks}/{PricePerBook}/{DateCreationBasket}/{DateUbdateBasket}")]
        public Baskets CreateDatabaseBaskets(Guid IdUser, Guid IdBook, int QuantityBooks, int PricePerBook, DateTime DateCreationBasket, DateTime DateUbdateBasket)
        {
            Baskets _baskets = new Baskets();

            return _baskets;



        }
        [Route("CreateDatabaseBookCard/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{RecieptDateBook}/{GenreBook}/{DescriptionBook}/{PriceBook}/{DateCreationBook}/{DateUpdateBook}")]
        public BookCard CreateDatabaseBookCard(string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, DateTime RecieptDateBook, string GenreBook, string DescriptionBook, decimal PriceBook, DateTime DateCreationBook, DateTime DateUpdateBook)
        {

            BookCard bookCard = new BookCard();
            return bookCard;

        }


        [Route("CreateDatabaseOrderCard/{OrderCardBooksList}/{DateCreationOrderCard}/{DateUpdateOrderCard}/{StatusOrderCard}/{IdUsers}")]
        public OrderCard CreateDatabaseOrderCard(String OrderCardBooksList, DateTime DateCreationOrderCard, DateTime DateUpdateOrderCard, string StatusOrderCard, Guid IdUsers)
        {
            OrderCard orderCard = new OrderCard();
            return orderCard;

        }

        [Route("CreateDatabaseQuoteCard/{QuoteTitle}/{QuoteText}/{QuoteAutor}/{DateCreationQuote}/{DateUpdateQuote}")]
        public QuoteCard CreateDatabaseQuoteCard(string QuoteTitle, string QuoteText, string QuoteAutor, DateTime DateCreationQuote, DateTime DateUpdateQuote)
        {
            QuoteCard quoteCard = new QuoteCard();

            return quoteCard;
        }

        [Route("CreateDatabaseRequestCard/{CommentTextCard}/{NumberStars}/{IdUser}/{IdBook}/{DateRequestCreation}/{DateRequestUpdation}")]
        public RequestCard CreateDatabaseRequestCard(string CommentTextCard, int NumberStars, Guid IdUser, Guid IdBook, DateTime DateRequestCreation, DateTime DateRequestUpdation)
        {

            RequestCard requestCard = new RequestCard();
            return requestCard;
        }

        [Route("CreateDatabaseUserCar/{UserName}/{SurnameUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{DateCreationUser}/{UpdateDateUser}")]
        public UserCard CreateDatabaseUserCard(string UserName, string SurnameUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime DateCreationUser, DateTime UpdateDateUser)
        {

            UserCard userCard = new UserCard();
            return userCard;

        }

        [Route("IDReadDatabaseBaskets/{IdBasket}")]
        public Baskets IDReadDatabaseBaskets(Guid IdBasket)

        {
            Baskets baskets = new Baskets();
            return baskets;

        }

        [Route("IDReadDatabaseBookCard/{IdBook}")]
        public BookCard IDReadDatabaseBookCard(Guid IdBook)
        {
            BookCard bookCard = new BookCard();
            return bookCard;

        }


        [Route("IDReadDatabaseOrderCard/{IdOrder}")]
        public OrderCard IDReadDatabaseOrderCard(Guid IdOrder)
        {
            OrderCard orderCard = new OrderCard();
            return orderCard;

        }


        [Route("IDReadDatabaseQuoteCard/{IdQuote}")]
        public QuoteCard IDReadDatabaseQuoteCard(Guid IdQuote)
        {
            QuoteCard quoteCard = new QuoteCard();
            return quoteCard;

        }


        [Route("IDReadDatabaseRequestCard/{IdRequestCard}")]
        public RequestCard IDReadDatabaseRequestCard(Guid IdRequestCard)
        {
            RequestCard requestCard = new RequestCard();
            return requestCard;

        }

        [Route("IDReadDatabaseUserCard/{IdUser}")]
        public UserCard IDReadDatabaseUserCard(Guid IdUser)
        {
            UserCard userCard = new UserCard();
            return userCard;

        }

        [Route("UpdateDatabaseBaskets/{IdBasket}/{IdUser}/{IdBook}/{QuantityBooks}/{PricePerBook}/{DateCreationBasket}/{DateUbdateBasket}")]
        public Baskets UpdateDatabaseBaskets(Guid IdBasket, Guid IdUser, Guid IdBook, int QuantityBooks, int PricePerBook, DateTime DateCreationBasket, DateTime DateUbdateBasket)
        {
            Baskets baskets = new Baskets();
            return baskets;

        }





        [Route("UpdateDatabaseBookCard/{IdBook}/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{RecieptDateBook}/{GenreBook}/{DescriptionBook}/{PriceBook}/{DateCreationBook}/{DateUpdateBook}")]
        public BookCard UpdateDatabaseBookCard(Guid IdBook, string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, DateTime RecieptDateBook, string GenreBook, string DescriptionBook, decimal PriceBook, DateTime DateCreationBook, DateTime DateUpdateBook)
        {
            BookCard bookCard = new BookCard();
            return bookCard;
        }

        [Route("UpdateDatabaseOrderCard/{IdOrder}/{OrderCardBooksList}/{DateCreationOrderCard}/{DateUpdateOrderCard}/{StatusOrderCard}/{IdUsers}")]
        public OrderCard UpdateDatabaseOrderCard(Guid IdOrder, String OrderCardBooksList, DateTime DateCreationOrderCard, DateTime DateUpdateOrderCard, string StatusOrderCard, Guid IdUsers)
        {
            OrderCard orderCard = new OrderCard();
            return orderCard;

        }

        [Route("UpdateDatabaseQuoteCard/{IdQuote}/{QuoteTitle}/{QuoteText}/{QuoteAutor}/{DateCreationQuote}/{DateUpdateQuote}")]
        public QuoteCard UpdateDatabaseQuoteCard(Guid IdQuote, string QuoteTitle, string QuoteText, string QuoteAutor, DateTime DateCreationQuote, DateTime DateUpdateQuote)
        {
            QuoteCard quoteCard = new QuoteCard();
            return quoteCard;

        }


        [Route("UpdateDatabaseRequestCard/{IdRequestCard}/{CommentTextCard}/{NumberStars}/{IdUser}/{IdBook}/{DateRequestCreation}/{DateRequestUpdation}")]
        public RequestCard UpdateDatabaseRequestCard(Guid IdRequestCard, string CommentTextCard, int NumberStars, Guid IdUser, Guid IdBook, DateTime DateRequestCreation, DateTime DateRequestUpdation)
        {
            RequestCard requestCard = new RequestCard();
            return requestCard;
        }

        [Route("UpdateDatabaseUserCard/{IdUser}/{UserName}/{SurnameUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{DateCreationUser}/{UpdateDateUser}")]
        public UserCard UpdateDatabaseUserCard(Guid IdUser, string UserName, string SurnameUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime DateCreationUser, DateTime UpdateDateUser)
        {
            UserCard userCard = new UserCard();
            return userCard;
           
        }

        [Route("DeleteDatabaseBaskets/{IdBasket}")]
        public Baskets DeleteDatabaseBaskets(Guid IdBasket)
        {
            Baskets baskets = new Baskets();
            return baskets;

        }

        [Route("DeleteDatabaseBookCard/{IdBook}")]
        public BookCard DeleteDatabaseBookCard(Guid IdBook)
        {
            BookCard bookCard = new BookCard();
            return bookCard;


        }

        [Route("DeleteDatabaseOrderCard/{IdOrder}")]
        public OrderCard DeleteDatabaseOrderCard(Guid IdOrder)
        {
            OrderCard orderCard = new OrderCard();
            return orderCard;

        }

        [Route("DeleteDatabaseQuoteCard/{IdQuote}")]
        public QuoteCard DeleteDatabaseQuoteCard(Guid IdQuote) 
        {
            QuoteCard quoteCard = new QuoteCard();
            return quoteCard;
        }


        [Route("DeleteDatabaseRequestCard(/{IdRequestCard}")]
        public RequestCard DeleteDatabaseRequestCard(Guid IdRequestCard) 
        {
            RequestCard requestCard = new RequestCard();
            return requestCard;


        }

        [Route("DeleteDatabaseUserCard(/{IdUser}")]
        public UserCard DeleteDatabaseUserCard(Guid IdUser)
        {
            UserCard userCard = new UserCard();

            return userCard;
         }




    }
}
