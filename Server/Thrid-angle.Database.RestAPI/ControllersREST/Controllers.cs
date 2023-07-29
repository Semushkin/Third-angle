using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
//using System.Web.Mvc;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Routing;
using Thrid_angle.Database.RestAPI.DTO;
using Thrid_angle.Database.RestAPI.Mehtods;

namespace Thrid_angle.Database.RestAPI.ControllersREST
{
    [Route("/Controllers/")]
    public class Controllers :  ControllerBase, IControllers
    {

        MethodsEntityFrameworcSQLite methodsEntityFrameworcSQLite;

      public  Controllers()
        {
             methodsEntityFrameworcSQLite = new MethodsEntityFrameworcSQLite();


        }


        [HttpPost]
        [Route("CreateDatabaseBaskets/{IdUser}/{IdBook}/{QuantityBooks}/{PricePerBook}/{DateCreationBasket}/{DateUbdateBasket}")]
        public void CreateDatabaseBaskets(Guid IdUser, Guid IdBook, int QuantityBooks, int PricePerBook, DateTime DateCreationBasket, DateTime DateUbdateBasket)
        {
            Baskets _baskets = new Baskets();
        
            _baskets.IdUser = IdUser;
            _baskets.IdBook = IdBook;
            _baskets.QuantityBooks = QuantityBooks;
            _baskets.PricePerBook = PricePerBook;
            _baskets.DateCreationBasket = DateCreationBasket;
            _baskets.DateUbdateBasket = DateUbdateBasket;


             methodsEntityFrameworcSQLite.CreateDatabaseBaskets(_baskets);


           



        }

        [HttpPost]
        [Route("CreateDatabaseBookCard/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{RecieptDateBook}/{GenreBook}/{DescriptionBook}/{PriceBook}/{DateCreationBook}/{DateUpdateBook}")]
        public void CreateDatabaseBookCard(string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, DateTime RecieptDateBook, string GenreBook, string DescriptionBook, decimal PriceBook, DateTime DateCreationBook, DateTime DateUpdateBook)
        {

            BookCard bookCard = new BookCard();

            bookCard.NameBook = NameBook;
            bookCard.AuthorBook = AuthorBook;
            bookCard.PhotoBook = PhotoBook;
            bookCard.VendorCodeBook = VendorCodeBook;
            bookCard.RecieptDateBook = RecieptDateBook;
            bookCard.GenreBook = GenreBook;
            bookCard.DescriptionBook = DescriptionBook;
            bookCard.PriceBook = PriceBook;
            bookCard.DateCreationBook = DateCreationBook;
            bookCard.DateUpdateBook = DateUpdateBook;
            

           methodsEntityFrameworcSQLite.CreateDatabaseBookCard(bookCard);

            

        }

        [HttpPost]
        [Route("CreateDatabaseOrderCard/{OrderCardBooksList}/{DateCreationOrderCard}/{DateUpdateOrderCard}/{StatusOrderCard}/{IdUsers}")]
        public void CreateDatabaseOrderCard(String OrderCardBooksList, DateTime DateCreationOrderCard, DateTime DateUpdateOrderCard, string StatusOrderCard, Guid IdUsers)
        {
            OrderCard orderCard = new OrderCard();

            orderCard.OrderCardBooksList = OrderCardBooksList;
            orderCard.DateCreationOrderCard = DateCreationOrderCard;
            orderCard.DateUpdateOrderCard = DateUpdateOrderCard;
            orderCard.StatusOrderCard = StatusOrderCard;
            orderCard.IdUsers = IdUsers;
            methodsEntityFrameworcSQLite.CreateDatabaseOrderCard(orderCard);

            

        }

        [HttpPost]
        [Route("CreateDatabaseQuoteCard/{QuoteTitle}/{QuoteText}/{QuoteAutor}/{DateCreationQuote}/{DateUpdateQuote}")]
        public void CreateDatabaseQuoteCard(string QuoteTitle, string QuoteText, string QuoteAutor, DateTime DateCreationQuote, DateTime DateUpdateQuote)
        {

           QuoteCard quoteCard = new QuoteCard();

            quoteCard.QuoteTitle = QuoteTitle;
            quoteCard.QuoteText = QuoteText;
            quoteCard.QuoteAutor = QuoteAutor;
            quoteCard.DateCreationQuote = DateCreationQuote;
            quoteCard.DateUpdateQuote = DateUpdateQuote;

            methodsEntityFrameworcSQLite.CreateDatabaseQuoteCard(quoteCard);

            
        }

        [HttpPost]
        [Route("CreateDatabaseRequestCard/{CommentTextCard}/{NumberStars}/{IdUser}/{IdBook}/{DateRequestCreation}/{DateRequestUpdation}")]
        public void CreateDatabaseRequestCard(string CommentTextCard, int NumberStars, Guid IdUser, Guid IdBook, DateTime DateRequestCreation, DateTime DateRequestUpdation)
        {

            RequestCard requestCard = new RequestCard();

            requestCard.CommentTextCard = CommentTextCard;
            requestCard.NumberStars = NumberStars;
            requestCard.IdUser = IdUser;
            requestCard.IdBook = IdBook;
            requestCard.DateRequestCreation = DateRequestCreation;
            requestCard.DateRequestUpdation = DateRequestUpdation;

            methodsEntityFrameworcSQLite.CreateDatabaseRequestCard(requestCard);

            
        }

        [HttpPost]
        [Route("CreateDatabaseUserCar/{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{DateCreationUser}/{UpdateDateUser}")]
        public void CreateDatabaseUserCard(string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime DateCreationUser, DateTime UpdateDateUser)
        {

            UserCard userCard = new UserCard();

            userCard.UserName = UserName;
            userCard.SurnameUser = SurnameUser;
            userCard.RoleUser = RoleUser;
            userCard.FloorUser = FloorUser;
            userCard.AgeUser = AgeUser;
            userCard.AddressUser = AddressUser;
            userCard.TelephoneUser = TelephoneUser;
            userCard.EmailUser = EmailUser;
            userCard.LoginUser = LoginUser;
            userCard.PasswordUser = PasswordUser;
            userCard.DateCreationUser = DateCreationUser;
            userCard.UpdateDateUser = UpdateDateUser;

            methodsEntityFrameworcSQLite.CreateDatabaseUserCard(userCard);


            

        }

        [HttpGet]
        [Route("IDReadDatabaseBaskets/{IdBasket}")]
        public Baskets IDReadDatabaseBaskets(Guid IdBasket)

        {
            Baskets baskets = methodsEntityFrameworcSQLite.IDReadDatabaseBaskets(IdBasket);
            return baskets;

        }

        [HttpGet]
        [Route("IDReadDatabaseBookCard/{IdBook}")]
        public BookCard IDReadDatabaseBookCard(Guid IdBook)
        {
            BookCard bookCard = methodsEntityFrameworcSQLite.IDReadDatabaseBookCard(IdBook);
            return bookCard;

        }

        [HttpGet]
        [Route("IDReadDatabaseOrderCard/{IdOrder}")]
        public OrderCard IDReadDatabaseOrderCard(Guid IdOrder)
        {
            OrderCard orderCard = methodsEntityFrameworcSQLite.IDReadDatabaseOrderCard(IdOrder);
            return orderCard;

        }

        [HttpGet]
        [Route("IDReadDatabaseQuoteCard/{IdQuote}")]
        public QuoteCard IDReadDatabaseQuoteCard(Guid IdQuote)
        {
            QuoteCard quoteCard = methodsEntityFrameworcSQLite.IDReadDatabaseQuoteCard(IdQuote);
            return quoteCard;

        }

        [HttpGet]
        [Route("IDReadDatabaseRequestCard/{IdRequestCard}")]
        public RequestCard IDReadDatabaseRequestCard(Guid IdRequestCard)
        {
            RequestCard requestCard = methodsEntityFrameworcSQLite.IDReadDatabaseRequestCard(IdRequestCard);
            return requestCard;

        }
        [HttpGet]
        [Route("IDReadDatabaseUserCard/{IdUser}")]
        public UserCard IDReadDatabaseUserCard(Guid IdUser)
        {
            UserCard userCard = methodsEntityFrameworcSQLite.IDReadDatabaseUserCard(IdUser);
            return userCard;

        }

        [HttpPut]
        [Route("UpdateDatabaseBaskets/{IdBasket}/{QuantityBooks}/{PricePerBook}/{DateUbdateBasket}")]
        public void UpdateDatabaseBaskets(Guid IdBasket, int QuantityBooks, int PricePerBook, DateTime DateUbdateBasket)
        {
            Baskets baskets = new Baskets();

            baskets.IdBasket = IdBasket;
            baskets.QuantityBooks = QuantityBooks;
            baskets.PricePerBook = PricePerBook;
            baskets.DateUbdateBasket = DateUbdateBasket;

            methodsEntityFrameworcSQLite.UpdateDatabaseBaskets(baskets);

           

        }




        [HttpPut]
        [Route("UpdateDatabaseBookCard/{IdBook}/{NameBook}/{AuthorBook}/{PhotoBook}/{VendorCodeBook}/{RecieptDateBook}/{GenreBook}/{DescriptionBook}/{PriceBook}/{DateUpdateBook}")]
       public void UpdateDatabaseBookCard(Guid IdBook, string NameBook, string AuthorBook, int PhotoBook, string VendorCodeBook, DateTime RecieptDateBook, string GenreBook, string DescriptionBook, decimal PriceBook,  DateTime DateUpdateBook)
       {
           BookCard bookCard = new BookCard();
            bookCard.IdBook = IdBook;
            bookCard.NameBook = NameBook;
            bookCard.AuthorBook = AuthorBook;
            bookCard.PhotoBook = PhotoBook;
            bookCard.VendorCodeBook = VendorCodeBook;
            bookCard.RecieptDateBook = RecieptDateBook;
            bookCard.GenreBook = GenreBook;
            bookCard.DescriptionBook = DescriptionBook;
            bookCard.PriceBook = PriceBook;
            bookCard.DateUpdateBook = DateUpdateBook;

            methodsEntityFrameworcSQLite.UpdateDatabaseBookCard(bookCard);

           
       }
     
        [HttpPut]
       [Route("UpdateDatabaseOrderCard/{IdOrder}/{OrderCardBooksList}/{DateUpdateOrderCard}/{StatusOrderCard}")]
       public void UpdateDatabaseOrderCard(Guid IdOrder, String OrderCardBooksList,  DateTime DateUpdateOrderCard, string StatusOrderCard)
       {

           OrderCard orderCard = new OrderCard();

            orderCard.IdOrder = IdOrder;
            orderCard.OrderCardBooksList = OrderCardBooksList;
            orderCard.DateUpdateOrderCard = DateUpdateOrderCard;
            orderCard.StatusOrderCard = StatusOrderCard;


            methodsEntityFrameworcSQLite.UpdateDatabaseOrderCard(orderCard);
           
     
       }
        
        [HttpPut]
       [Route("UpdateDatabaseQuoteCard/{IdQuote}/{QuoteTitle}/{QuoteText}/{QuoteAutor}/{DateUpdateQuote}")]
       public void UpdateDatabaseQuoteCard(Guid IdQuote, string QuoteTitle, string QuoteText, string QuoteAutor, DateTime DateUpdateQuote)
       {
           QuoteCard quoteCard = new QuoteCard();

            quoteCard.IdQuote = IdQuote;
            quoteCard.QuoteTitle = QuoteTitle;
            quoteCard.QuoteText = QuoteText;
            quoteCard.QuoteAutor = QuoteAutor;
            quoteCard.DateUpdateQuote = DateUpdateQuote;

            methodsEntityFrameworcSQLite.UpdateDatabaseQuoteCard(quoteCard);

           
     
       }
     
        [HttpPut]
       [Route("UpdateDatabaseRequestCard/{IdRequestCard}/{CommentTextCard}/{NumberStars}/{DateRequestUpdation}")]
       public void UpdateDatabaseRequestCard(Guid IdRequestCard, string CommentTextCard, int NumberStars,  DateTime DateRequestUpdation)
       {
           RequestCard requestCard = new RequestCard();

            requestCard.IdRequestCard = IdRequestCard;
            requestCard.CommentTextCard = CommentTextCard;
            requestCard.NumberStars = NumberStars;
            requestCard.DateRequestUpdation = DateRequestUpdation;

            methodsEntityFrameworcSQLite.UpdateDatabaseRequestCard(requestCard);

           
       }
     
       [HttpPut]
       [Route("UpdateDatabaseUserCard/{IdUser}/{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{UpdateDateUser}")]
       public void UpdateDatabaseUserCard(Guid IdUser, string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime UpdateDateUser)
       {
           UserCard userCard = new UserCard();

            userCard.IdUser = IdUser;
            userCard.UserName = UserName;
            userCard.SurnameUser = SurnameUser;
            userCard.RoleUser = RoleUser;
            userCard.FloorUser = FloorUser;
            userCard.AgeUser = AgeUser;
            userCard.AddressUser = AddressUser;
            userCard.TelephoneUser = TelephoneUser;
            userCard.EmailUser = EmailUser;
            userCard.LoginUser = LoginUser;
            userCard.PasswordUser = PasswordUser;
            userCard.UpdateDateUser = UpdateDateUser;

            methodsEntityFrameworcSQLite.UpdateDatabaseUserCard(userCard);
           
          
       }
     
       [HttpDelete]
       [Route("DeleteDatabaseBaskets/{IdBasket}")]
       public void DeleteDatabaseBaskets(Guid IdBasket)
       {
           
            methodsEntityFrameworcSQLite.DeleteDatabaseBaskets(IdBasket);
          
     
       }

        [HttpDelete]
        [Route("DeleteDatabaseBookCard/{IdBook}")]
       public void DeleteDatabaseBookCard(Guid IdBook)
       {
           
            methodsEntityFrameworcSQLite.DeleteDatabaseBookCard(IdBook);
           
       }

        [HttpDelete]
        [Route("DeleteDatabaseOrderCard/{IdOrder}")]
       public void DeleteDatabaseOrderCard(Guid IdOrder)
       {
           
            methodsEntityFrameworcSQLite.DeleteDatabaseOrderCard(IdOrder);
           
     
       }

        [HttpDelete]
        [Route("DeleteDatabaseQuoteCard/{IdQuote}")]
        public void DeleteDatabaseQuoteCard(Guid IdQuote)
        {
            methodsEntityFrameworcSQLite.DeleteDatabaseQuoteCard(IdQuote);
        }

        [HttpDelete]
        [Route("DeleteDatabaseRequestCard(/{IdRequestCard}")]
       public void DeleteDatabaseRequestCard(Guid IdRequestCard) 
       {
            methodsEntityFrameworcSQLite.DeleteDatabaseRequestCard(IdRequestCard);

     
     
       }

        [HttpDelete]
        [Route("DeleteDatabaseUserCard(/{IdUser}")]
       public   void DeleteDatabaseUserCard(Guid IdUser)
       {

            methodsEntityFrameworcSQLite.DeleteDatabaseUserCard(IdUser);
          
        }




    }
}
