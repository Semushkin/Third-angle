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
            modelBuilder.Entity<Baskets>()
                .HasKey(b => b.IdBasket);

            modelBuilder.Entity<OrderCard>()
               .HasKey(b => b.IdOrder);

            modelBuilder.Entity<RequestCard>()
            .HasKey(b => b.IdRequestCard);

            
                modelBuilder.Entity<UserCard>()
            .HasKey(b => b.IdUser);

            modelBuilder.Entity<QuoteCard>()
          .HasKey(b => b.IdQuote);

           
                 modelBuilder.Entity<BookCard>()
          .HasKey(b => b.IdBook);



        }


    } 

}

