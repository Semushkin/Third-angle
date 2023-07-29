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
    public class RequestCard // карточка запроса
    {
        [Key]
        public Guid IdRequestCard { get ; set; }
        public string CommentTextCard { get; set; }
        public int? NumberStars { get; set; } // количество звездочек
        public Guid? IdUser { get; set; }
        public Guid? IdBook { get; set; }
        public DateTime? DateRequestCreation { get; set; }
        public DateTime? DateRequestUpdation { get; set; }
    }
}
