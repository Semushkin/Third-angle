using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Thrid_angle.Database.RestAPI.Migrations
{
    /// <inheritdoc />
    public partial class NewMigration : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Baskets",
                columns: table => new
                {
                    IdBasket = table.Column<Guid>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Baskets", x => x.IdBasket);
                });

            migrationBuilder.CreateTable(
                name: "BookCard",
                columns: table => new
                {
                    IdBook = table.Column<Guid>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_BookCard", x => x.IdBook);
                });

            migrationBuilder.CreateTable(
                name: "OrderCard",
                columns: table => new
                {
                    IdOrder = table.Column<Guid>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_OrderCard", x => x.IdOrder);
                });

            migrationBuilder.CreateTable(
                name: "QuoteCard",
                columns: table => new
                {
                    IdQuote = table.Column<Guid>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_QuoteCard", x => x.IdQuote);
                });

            migrationBuilder.CreateTable(
                name: "RequestCard",
                columns: table => new
                {
                    IdRequestCard = table.Column<Guid>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_RequestCard", x => x.IdRequestCard);
                });

            migrationBuilder.CreateTable(
                name: "UserCard",
                columns: table => new
                {
                    IdUser = table.Column<Guid>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_UserCard", x => x.IdUser);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Baskets");

            migrationBuilder.DropTable(
                name: "BookCard");

            migrationBuilder.DropTable(
                name: "OrderCard");

            migrationBuilder.DropTable(
                name: "QuoteCard");

            migrationBuilder.DropTable(
                name: "RequestCard");

            migrationBuilder.DropTable(
                name: "UserCard");
        }
    }
}
