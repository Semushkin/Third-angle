using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thrid_angle.Database.RestAPI.DTO
{
    [Table("Baskets")]
    public class Baskets
    {
        [Key]
        public Guid IdBasket { get; set; }
        public Guid? IdUser { get; set; }
        public Guid? IdBook { get; set; }
        public Guid? NumberOrderCard { get; set; }
        public string? StatusOrderCard { get; set; }
        public int? NumberCard { get; set; }
        public int? QuantityBooks { get; set; }
        public int? PricePerBook { get; set; }  // цена за книгу
        public DateTime? DateCreationBasket { get; set; }
        public DateTime? DateUbdateBasket { get; set; }

    }
}
