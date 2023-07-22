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
    [Table("UserCard")]
    public class UserCard
    {
        [Key]
        public Guid IdUser { get; set; }
        public string UserName { get; set; }
        public string SurnameUser { get; set; }
        public string FloorUser { get; set; }
        public int AgeUser { get; set; }
        public string AddressUser { get; set;}
        public string TelephoneUser { get; set; }
        public string EmailUser { get; set; }
        public string LoginUser { get; set; }
        public string PasswordUser { get; set; }
        public DateTime DateCreationUser { get; set; }
        public DateTime UpdateDateUser { get; set; }
        
    }
   
}
