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

        internal void CreateDatabaseSQLite(dynamic table) 
        {
            


               if (table is Baskets) { db.Add(table); db.SaveChanges(); }
               //if (table is BookCard) { db.Add(table); db.SaveChanges(); }
               //if (table is OrderCard) { db.Add(table); db.SaveChanges(); }
               //if (table is QuoteCard) { db.Add(table); db.SaveChanges(); }
               //if (table is RequestCard) { db.Add(table); db.SaveChanges(); }
               //if (table is UserCard) { db.Add(table); db.SaveChanges(); }




        }


               
           
            

            



        



        void ReadDatabaseSQLite(dynamic table)
        {
            List<Baskets> baskets = new List<Baskets>();

            if (table is Baskets) { baskets = db.DbBaskets.ToList<Baskets>(); }
            if (table is Baskets) { db.Add(table); db.SaveChanges(); }
            if (table is Baskets) { db.Add(table); db.SaveChanges(); }
            if (table is Baskets) { db.Add(table); db.SaveChanges(); }
            if (table is Baskets) { db.Add(table); db.SaveChanges(); }
            if (table is Baskets) { db.Add(table); db.SaveChanges(); }



        }



    }
}
