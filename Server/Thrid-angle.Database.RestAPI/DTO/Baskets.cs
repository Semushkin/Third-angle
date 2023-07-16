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
    internal class Baskets
    {
        [Key]
        internal Guid IdBasket { get; set; }
        internal Guid IdUser { get; set; }
        internal Guid IdBook { get; set; }
        internal int QuantityBooks { get; set; }
        internal int PricePerBook { get; set; }  // цена за книгу
        internal DateTime DateCreationBasket { get; set; }
        internal DateTime DateUbdateBasket { get; set; }

    }
}
