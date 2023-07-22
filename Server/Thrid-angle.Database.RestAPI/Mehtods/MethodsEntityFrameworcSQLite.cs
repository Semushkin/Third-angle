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
     internal void CreateDatabaseOrderCard(OrderCard table) { db.Add(table); db.SaveChanges(); }
     internal void CreateDatabaseQuoteCard(QuoteCard table) { db.Add(table); db.SaveChanges(); }
     internal void CreateDatabaseRequestCard(RequestCard table) { db.Add(table); db.SaveChanges(); }
     internal void CreateDatabaseUserCard(UserCard table)  {db.Add(table); db.SaveChanges();}


        internal List<Baskets> ReadDatabaseBaskets() { List<Baskets> t = db.DbBaskets.ToList<Baskets>(); return t;  }
        internal List<BookCard> ReadDatabaseBookCard() { List<BookCard> t = db.DbBookCard.ToList<BookCard>(); return t; }
        internal List<OrderCard> ReadDatabaseOrderCard() { List<OrderCard> t = db.DbOrderCard.ToList<OrderCard>(); return t; }
        internal List<QuoteCard> ReadDatabaseQuoteCard() { List<QuoteCard> t = db.DbQuoteCard.ToList<QuoteCard>(); return t; }
        internal List<RequestCard> ReadDatabaseRequestCard() { List<RequestCard> t = db.DbRequestCard.ToList<RequestCard>(); return t; }
        internal List<UserCard> ReadDatabaseUserCard() { List<UserCard> t = db.DbUserCard.ToList<UserCard>(); return t; }

        internal Baskets IDReadDatabaseBaskets(Guid Id) { Baskets t = db.DbBaskets.Find(Id); return t; }
        internal BookCard IDReadDatabaseBookCard(Guid Id) { BookCard t = db.DbBookCard.Find(Id); return t; }
        internal OrderCard IDReadDatabaseOrderCard(Guid Id) { OrderCard t = db.DbOrderCard.Find(Id); return t; }
        internal QuoteCard IDReadDatabaseQuoteCard(Guid Id) { QuoteCard t = db.DbQuoteCard.Find(Id); return t; }
        internal RequestCard IDReadDatabaseRequestCard(Guid Id) { RequestCard t =  db.DbRequestCard.Find(Id); return t; }
        internal UserCard IDReadDatabaseUserCard(Guid Id) { UserCard t = db.DbUserCard.Find(Id); return t; }


        internal void UpdateDatabaseBaskets(Baskets baskets) { db.DbBaskets.Add(baskets); db.SaveChanges(); }
        internal void UpdateDatabaseBookCard(BookCard bookCard) { db.DbBookCard.Add(bookCard); db.SaveChanges(); }
        internal void UpdateDatabaseOrderCard(OrderCard orderCard) { db.DbOrderCard.Add(orderCard); db.SaveChanges(); }
        internal void UpdateDatabaseQuoteCard(QuoteCard quoteCard) { db.DbQuoteCard.Add(quoteCard); db.SaveChanges(); }
        internal void UpdateDatabaseRequestCard(RequestCard requestCard) { db.DbRequestCard.Add(requestCard); db.SaveChanges(); }
        internal void UpdateDatabaseUserCard(UserCard userCard) { db.DbUserCard.Add(userCard); }

        internal void DeleteDatabaseBaskets(Guid Id) { db.DbBaskets.Where(d => d.IdBasket == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseBookCard(Guid Id) { db.DbBookCard.Where(d => d.IdBook == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseOrderCard(Guid Id) { db.DbOrderCard.Where(d => d.IdOrder == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseQuoteCard(Guid Id) { db.DbQuoteCard.Where(d => d.IdQuote == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseRequestCard(Guid Id) { db.DbRequestCard.Where(d => d.IdRequestCard == Id).ExecuteDelete(); db.SaveChanges(); }
        internal void DeleteDatabaseUserCard(Guid Id) { db.DbUserCard.Where(d => d.IdUser == Id).ExecuteDelete(); db.SaveChanges(); }


    }
}
