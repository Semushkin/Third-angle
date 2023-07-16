using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore.Sqlite;

namespace Thrid_angle.Database.RestAPI.DTO
{
    [Table("RequestCard")]
    internal class RequestCard // карточка запроса
    {
        [Key]
        internal Guid IdRequestCard { get ; set; }
        internal  string CommentTextCard { get; set; }
        internal int NumberStars { get; set; } // количество звездочек
        internal Guid IdUser { get; set; }
        internal Guid IdBook { get; set; }
        internal DateTime DateRequestCreation { get; set; }
        internal DateTime DateRequestUpdation { get; set; }
    }
}
