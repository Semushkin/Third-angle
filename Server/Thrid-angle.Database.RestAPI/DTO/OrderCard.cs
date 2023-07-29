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
    public class OrderCard // карточка заказа
    {
        [Key]
        public Guid IdOrder { get ; set ; }
        public String OrderCardBooksList { get; set; } // список книг заказа
        public DateTime? DateCreationOrderCard { get; set; }
        public DateTime? DateUpdateOrderCard { get; set; }
        public string StatusOrderCard { get; set; }
        public Guid? IdUsers { get; set; }
    }
}
