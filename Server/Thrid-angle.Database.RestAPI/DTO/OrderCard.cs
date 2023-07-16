using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thrid_angle.Database.RestAPI.DTO
{
    [Table("OrderCard")]
    internal class OrderCard // карточка заказа
    {
        [Key]
        internal Guid IdOrder { get ; set ; }
        internal String OrderCardBooksList { get; set; } // список книг заказа
        internal DateTime DateCreationOrderCard { get; set; }
        internal DateTime DateUpdateOrderCard { get; set; }
        internal string StatusOrderCard { get; set; }
        internal Guid IdUsers { get; set; }
    }
}
