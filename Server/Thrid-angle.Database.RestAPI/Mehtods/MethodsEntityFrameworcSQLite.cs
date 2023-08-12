using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using Thrid_angle.Database.RestAPI.Database;
using System.Dynamic;
using Thrid_angle.Database.RestAPI.DTO;
using Microsoft.EntityFrameworkCore;
using Microsoft.Data.Sqlite;

namespace Thrid_angle.Database.RestAPI.Mehtods
{
    internal class MethodsEntityFrameworcSQLite
    {
        internal DatabaseContext db = new DatabaseContext();

         
     internal void CreateDatabaseBaskets(Baskets table) { db.Add(table); db.SaveChanges(); }
     internal void CreateDatabaseBookCard(BookCard table) { db.Add(table); db.SaveChanges(); }
     
     internal void CreateDatabaseQuoteCard(QuoteCard table) { db.Add(table); db.SaveChanges(); }
     internal void CreateDatabaseRequestCard(RequestCard table) { db.Add(table); db.SaveChanges(); }
     internal void CreateDatabaseUserCard(UserCard table)  {db.Add(table); db.SaveChanges();}


       
        internal List<BookCard> ReadDatabaseBookCard() { List<BookCard> t = db.DbBookCard.ToList<BookCard>(); return t; }
       
        internal List<QuoteCard> ReadDatabaseQuoteCard() { List<QuoteCard> t = db.DbQuoteCard.ToList<QuoteCard>(); return t; }
        internal List<RequestCard> ReadDatabaseRequestCard() { List<RequestCard> t = db.DbRequestCard.ToList<RequestCard>(); return t; }
        internal List<UserCard> ReadDatabaseUserCard() { List<UserCard> t = db.DbUserCard.ToList<UserCard>(); return t; }

        internal Baskets IDReadDatabaseBaskets(Guid Id) { Baskets t = db.DbBaskets.Find(Id); return t; } // - удалить
        internal BookCard IDReadDatabaseBookCard(Guid Id) { BookCard t = db.DbBookCard.Find(Id); return t; }
       
        internal QuoteCard IDReadDatabaseQuoteCard(Guid Id) { QuoteCard t = db.DbQuoteCard.Find(Id); return t; }
        internal RequestCard IDReadDatabaseRequestCard(Guid Id) { RequestCard t =  db.DbRequestCard.Find(Id); return t; }
        internal UserCard IDReadDatabaseUserCard(Guid Id) { UserCard t = db.DbUserCard.Find(Id); return t; }



        internal void UpdateDatabaseBaskets(Baskets baskets) 
        {


            db.DbBaskets.Where(d => d.IdBasket == baskets.IdBasket).Where(b=> b.StatusOrderCard== "basket").ExecuteUpdate(b => b.SetProperty(t => t.QuantityBooks, baskets.QuantityBooks));
            db.DbBaskets.Where(d => d.IdBasket == baskets.IdBasket).Where(b => b.StatusOrderCard == "basket").ExecuteUpdate(b => b.SetProperty(t => t.PricePerBook, baskets.PricePerBook));
            db.DbBaskets.Where(d => d.IdBasket == baskets.IdBasket).Where(b => b.StatusOrderCard == "basket").ExecuteUpdate(b => b.SetProperty(t => t.DateUbdateBasket, baskets.DateUbdateBasket));

            db.SaveChanges();

       }
       
     








    



    internal void UpdateDatabaseBookCard(BookCard bookCard) 
        {

            var _db = db.DbBookCard.Find(bookCard.IdBook);
            _db.NameBook = bookCard.NameBook;
            _db.AuthorBook = bookCard.AuthorBook;
            _db.PhotoBook = bookCard.PhotoBook;
            _db.VendorCodeBook = bookCard.VendorCodeBook;
            _db.RecieptDateBook = bookCard.RecieptDateBook;
            _db.GenreBook = bookCard.GenreBook;
            _db.DescriptionBook = bookCard.DescriptionBook;
            _db.PriceBook = bookCard.PriceBook;
           // _db.DateCreationBook = bookCard.DateCreationBook;
           _db.DateUpdateBook = bookCard.DateUpdateBook;

           db.SaveChanges();

        }

        internal void UpdateDatabaseOrderCard(Baskets baskets)
        {
            db.DbBaskets.Where(d => d.NumberOrderCard == baskets.NumberOrderCard).ExecuteUpdate(b => b.SetProperty(t => t.StatusOrderCard, baskets.StatusOrderCard));
            db.DbBaskets.Where(d => d.NumberOrderCard == baskets.NumberOrderCard).ExecuteUpdate(b => b.SetProperty(t => t.DateUbdateBasket, baskets.DateUbdateBasket));


           

            db.SaveChanges();


          

        }




        internal void UpdateDatabaseQuoteCard(QuoteCard quoteCard) 
        {
            var _db = db.DbQuoteCard.Find(quoteCard.IdQuote);

            _db.QuoteTitle = quoteCard.QuoteTitle;
            _db.QuoteText = quoteCard.QuoteText;
            _db.QuoteAutor = quoteCard.QuoteAutor;
           // _db.DateCreationQuote = quoteCard.DateCreationQuote;
            _db.DateUpdateQuote = quoteCard.DateUpdateQuote;
           ; db.SaveChanges(); 
        
        }

        internal void UpdateDatabaseRequestCard(RequestCard requestCard)
        {

            var _db = db.DbRequestCard.Find(requestCard.IdRequestCard);
            _db.CommentTextCard = requestCard.CommentTextCard;
            _db.NumberStars = requestCard.NumberStars;
           // _db.IdUser = requestCard.IdUser;
           // _db.IdBook = requestCard.IdBook;
            //_db.DateRequestCreation = requestCard.DateRequestCreation;
            _db.DateRequestUpdation = requestCard.DateRequestUpdation;
            db.SaveChanges();
        }

        internal void UpdateDatabaseUserCard(UserCard userCard)
        {
            var _db = db.DbUserCard.Find(userCard.IdUser);


            _db.UserName = userCard.UserName;
            _db.SurnameUser = userCard.SurnameUser;
            _db.RoleUser = userCard.RoleUser; 
            _db.FloorUser = userCard.FloorUser;
            _db.FloorUser = userCard.RoleUser;
            _db.AgeUser = userCard.AgeUser;
            _db.AddressUser = userCard.AddressUser;
            _db.TelephoneUser = userCard.TelephoneUser;
            _db.EmailUser = userCard.EmailUser;
            _db.LoginUser = userCard.LoginUser;
            _db.PasswordUser = userCard.PasswordUser;
            //_db.DateCreationUser = userCard.DateCreationUser;
            _db.UpdateDateUser = userCard.UpdateDateUser;
             db.SaveChanges();

        }

        internal void DeleteDatabaseBaskets(Guid Id) { db.DbBaskets.Where(d => d.IdBasket == Id&d.StatusOrderCard== "basket").ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseBookCard(Guid Id) { db.DbBookCard.Where(d => d.IdBook == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseOrderCard(Guid Id) { db.DbBaskets.Where(d => d.NumberOrderCard == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseQuoteCard(Guid Id) { db.DbQuoteCard.Where(d => d.IdQuote == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseRequestCard(Guid Id) { db.DbRequestCard.Where(d => d.IdRequestCard == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseUserCard(Guid Id) { db.DbUserCard.Where(d => d.IdUser == Id).ExecuteDelete(); db.SaveChanges(); }




        internal List<Baskets> UserReadDatabaseBaskets(Guid IdUser) { List<Baskets> t = db.DbBaskets.Where(d => d.IdUser == IdUser && d.StatusOrderCard == "basket").ToList<Baskets>(); return t; }


        internal List<Baskets> UserReadDatabaseOrderCard(Guid IdUser) { List<Baskets> t = db.DbBaskets.Where(d =>  d.IdUser == IdUser&&d.StatusOrderCard== "order").ToList<Baskets>(); return t; }


        internal List<RequestCard> IdUserReadDatabaseRequestCard(Guid IdUser) { List<RequestCard> t = db.DbRequestCard.Where(d => d.IdUser == IdUser).ToList<RequestCard>(); return t; }


        internal List<RequestCard> IdBookReadDatabaseRequestCard(Guid IdBook) { List<RequestCard> t = db.DbRequestCard.Where(d => d.IdBook == IdBook).ToList<RequestCard>(); return t; }


        internal List<UserCard> LoginUserReadDatabaseUserCard(string LoginUser, string PasswordUser) { List<UserCard> t = db.DbUserCard.Where(d => d.LoginUser == LoginUser&&d.PasswordUser== PasswordUser).ToList<UserCard>(); return t; }


        internal void CreateDatabaseBasketsStatusOrderCard(Guid IdUser)
        {
           
                var t = db.DbBaskets.Where(d => d.StatusOrderCard == "basket"& d.IdUser== IdUser);

                t.ExecuteUpdate(setters => setters.SetProperty(b => b.StatusOrderCard, "order"));

                db.SaveChanges();

            


        }




    }
}
