using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Thrid_angle.Database.RestAPI.DTO;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Sqlite;
using System.Reflection.Metadata;

namespace Thrid_angle.Database.RestAPI.Database
{
    internal class DatabaseContext : DbContext
    {
        public DbSet<Baskets> DbBaskets { get; set; }
        public DbSet<BookCard> DbBookCard { get; set; }
        public DbSet<OrderCard> DbOrderCard { get; set; }
        public DbSet<QuoteCard> DbQuoteCard { get; set; } 
        public DbSet<RequestCard> DbRequestCard { get; set; }
        public DbSet<UserCard> DbUserCard { get; set; }

        public string DbPath { get; }


        public DatabaseContext()
        {
            var folder = Environment.SpecialFolder.LocalApplicationData;
            string path = Environment.GetFolderPath(folder);
            DbPath = System.IO.Path.Join(path, "ThridAngle.db"); 
           
        }
        protected override void OnConfiguring(DbContextOptionsBuilder options) => options.UseSqlite($"Data Source={DbPath}");



        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Baskets>().HasKey(b => b.IdBasket);
            modelBuilder.Entity<Baskets>().Property(b=>b.IdUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<Baskets>().Property(b => b.IdBook).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<Baskets>().Property(b => b.QuantityBooks).IsRequired().HasMaxLength(10);
            modelBuilder.Entity<Baskets>().Property(b => b.PricePerBook).IsRequired().HasMaxLength(10);
            modelBuilder.Entity<Baskets>().Property(b => b.DateCreationBasket).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<Baskets>().Property(b => b.DateUbdateBasket).IsRequired().HasMaxLength(100);

        
            modelBuilder.Entity<OrderCard>().HasKey(b => b.IdOrder);
            modelBuilder.Entity<OrderCard>().Property(b=>b.OrderCardBooksList).IsRequired().HasMaxLength(300);
            modelBuilder.Entity<OrderCard>().Property(b => b.DateCreationOrderCard).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<OrderCard>().Property(b => b.DateUpdateOrderCard).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<OrderCard>().Property(b => b.StatusOrderCard).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<OrderCard>().Property(b => b.IdUsers).IsRequired().HasMaxLength(50);

       
            modelBuilder.Entity<RequestCard>().HasKey(b => b.IdRequestCard);
            modelBuilder.Entity<RequestCard>().Property(b => b.CommentTextCard).IsRequired().HasMaxLength(500);
            modelBuilder.Entity<RequestCard>().Property(b => b.NumberStars).IsRequired().HasMaxLength(10);
            modelBuilder.Entity<RequestCard>().Property(b => b.IdUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<RequestCard>().Property(b => b.IdBook).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<RequestCard>().Property(b => b.DateRequestCreation).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<RequestCard>().Property(b => b.DateRequestUpdation).IsRequired().HasMaxLength(100);

   
            modelBuilder.Entity<UserCard>().HasKey(b => b.IdUser);
            modelBuilder.Entity<UserCard>().Property(b => b.UserName).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<UserCard>().Property(b => b.SurnameUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<UserCard>().Property(b => b.RoleUser).IsRequired().HasMaxLength(20);
            modelBuilder.Entity<UserCard>().Property(b => b.FloorUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<UserCard>().Property(b => b.AgeUser).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<UserCard>().Property(b => b.AddressUser).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<UserCard>().Property(b => b.TelephoneUser).IsRequired().HasMaxLength(30);
            modelBuilder.Entity<UserCard>().Property(b => b.EmailUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<UserCard>().Property(b => b.LoginUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<UserCard>().Property(b => b.PasswordUser).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<UserCard>().Property(b => b.DateCreationUser).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<UserCard>().Property(b => b.UpdateDateUser).IsRequired().HasMaxLength(100);

        
    

            modelBuilder.Entity<QuoteCard>().HasKey(b => b.IdQuote);
            modelBuilder.Entity<QuoteCard>().Property(b => b.QuoteTitle).IsRequired().HasMaxLength(200);
            modelBuilder.Entity<QuoteCard>().Property(b => b.QuoteText).IsRequired().HasMaxLength(1000);
            modelBuilder.Entity<QuoteCard>().Property(b => b.QuoteAutor).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<QuoteCard>().Property(b => b.DateCreationQuote).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<QuoteCard>().Property(b => b.DateUpdateQuote).IsRequired().HasMaxLength(100);

       

           modelBuilder.Entity<BookCard>().HasKey(b => b.IdBook);
            modelBuilder.Entity<BookCard>().Property(b => b.NameBook).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<BookCard>().Property(b => b.AuthorBook).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<BookCard>().Property(b => b.PhotoBook).IsRequired().HasMaxLength(10);
            modelBuilder.Entity<BookCard>().Property(b => b.VendorCodeBook).IsRequired().HasMaxLength(50);
            modelBuilder.Entity<BookCard>().Property(b => b.RecieptDateBook).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<BookCard>().Property(b => b.GenreBook).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<BookCard>().Property(b => b.DescriptionBook).IsRequired().HasMaxLength(1000);
            modelBuilder.Entity<BookCard>().Property(b => b.PriceBook).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<BookCard>().Property(b => b.DateCreationBook).IsRequired().HasMaxLength(100);
            modelBuilder.Entity<BookCard>().Property(b => b.DateUpdateBook).IsRequired().HasMaxLength(100);









    }


    } 

}

